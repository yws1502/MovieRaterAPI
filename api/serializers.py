from rest_framework import serializers
from .models import *


class MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ('id', 'title', 'description')


class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = ('id', 'stars', 'user', 'movie')