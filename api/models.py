from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
  title = models.CharField(max_length=32)
  description = models.TextField(max_length=360)


class Rating(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
  
  class Meta:
    # A라는 user가 한 영화에 대해 리뷰를 남기면 A user는 다시 리뷰를 하지 못하게 하는 것!
    unique_together = (('user', 'movie'),)
    index_together = (('user', 'movie'),)