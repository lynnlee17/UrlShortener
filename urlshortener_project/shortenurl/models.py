from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Urls(models.Model):
    created = models.DateTimeField(default=timezone. now)
    short_url = models.SlugField(max_length=200, unique=True)
    actual_url = models.URLField(max_length=200)
    last_visited = models.DateTimeField(auto_now=True)
    visit_count = models.IntegerField(default=0)

def __str__(self):
    return self.actual_url