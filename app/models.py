from django.db import models
from django.db.models.fields import BooleanField, CharField, URLField

# Create your models here.

class Movies(models.Model):
    imgurl = URLField(max_length=200)
    title = CharField(max_length=100)
    runtime = CharField(max_length=50)
    medium = CharField(max_length=100)
    genre = CharField(max_length=100)
    source = CharField(max_length=100)
    watched = BooleanField(default=False)
    notes = CharField(max_length=255)