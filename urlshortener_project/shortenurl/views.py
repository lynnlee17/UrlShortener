from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.conf import settings
from django.template.context_processors import csrf

from urllib.parse import urlparse
import string, json
from shortenurl.models import Url


def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html', c)


def redirect_link(request, short_url):
    url_object = get_object_or_404(Url, short_url=short_url)
    # Find the url object or throw 404 error

    url_object.visit_count += 1
    # update visit count

    url_object.save()
    return HttpResponseRedirect(url_object.actual_url)


def shorten_url(request):
    url = request.POST.get("url", '')
    if not (url == ''):
        parsed_url = urlparse(url)
        # check to see if the url contains 'https:// or http://

        if (parsed_url.scheme == ''):
            url = "https://" + url

        if len(Url.objects.filter(actual_url=url)) == 1:
            b = Url.objects.get(actual_url=url)
            short_url = b.short_url
        else:
            a = Url.objects.last().id + 1
            # temp solution, for some reason can't create the object and get the id,
            # so I looked for the last id and add 1 for the next id in the database
            short_url = get_short_url(a)
            b = Url.objects.create(actual_url=url, short_url=short_url).save()

        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + short_url
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}), content_type="application/json")



def get_short_url(num):
    # taken from https://stackoverflow.com/questions/1119722/base-62-conversion
    # takes the id from the database where the url is stored, and turns the integer
    # into a base62 string and returns that as the short_url

    base = tuple(string.ascii_uppercase + string.digits + string.ascii_lowercase)
    base_dict = dict((c, v) for v, c in enumerate(base))
    b = 62

    short_url = ""
    while num:
        num, rem = divmod(num, b)
        short_url = base[rem] + short_url
    return short_url