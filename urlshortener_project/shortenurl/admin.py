from django.contrib import admin
from shortenurl.models import Url
# Register your models here.

class UrlAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'short_url', 'actual_url', 'last_visited', 'visit_count')
    ordering = ('-created',)

admin.site.register(Url, UrlAdmin)
