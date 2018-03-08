"""urlshortener_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from shortenurl import views

app_name = 'shortenurl'

urlpatterns = [
    url(r'^$', views.index, name='home'),
    #leads to main homepage
    url(r'^(?P<short_url>\w{0,200})$', views.redirect_link, name='redirectoriginal'),
    #append the short url and it will redirect to the original link
    url(r'^shorten/$', views.shorten_url, name='shortenurl'),
    #create short url from the original and return it
]
