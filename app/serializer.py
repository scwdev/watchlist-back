from .models import Movies
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class MovieSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Movies
        fields = "__all__"
