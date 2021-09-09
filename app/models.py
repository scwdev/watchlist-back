from django.db import models
from django.db.models.fields import BooleanField, CharField, URLField

# Create your models here.

class Movies(models.Model):
    imgurl = URLField(max_length=200, blank=True)
    title = CharField(max_length=100, blank=True)
    runtime = CharField(max_length=50, blank=True)
    medium = CharField(max_length=100, blank=True)
    genre = CharField(max_length=100, blank=True)
    source = CharField(max_length=100, blank=True)
    watched = BooleanField(default=False)
    notes = CharField(max_length=255, blank=True)