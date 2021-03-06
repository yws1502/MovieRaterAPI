from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import *
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer
  authentication_classes = (TokenAuthentication, )
  permission_classes = (AllowAny, )

  @action(detail=True, methods=['POST'])
  def rate_movie(self, request, pk=None):
    if 'stars' not in request.data:
      response = {'message': 'You need to provide stars'}
      return Response(response, status=status.HTTP_400_BAD_REQUEST)

    else:
      movie = Movie.objects.get(id=pk)
      user = request.user
      stars = request.data['stars']
      message = 'Rating updated'

      try: # update
        rating = Rating.objects.get(user=user.id, movie=movie.id)
        rating.stars = stars
        rating.save()
      except: # create
        rating = Rating.objects.create(user=user, movie=movie, stars=stars)
        message = 'Rating created'

      serializer = RatingSerializer(rating, many=False)
      response = {
        'message': message,
        'result': serializer.data,
      }
      return Response(response, status=status.HTTP_200_OK)
  

class RatingViewSet(viewsets.ModelViewSet):
  queryset = Rating.objects.all()
  serializer_class = RatingSerializer
  authentication_classes = (TokenAuthentication, )
  permission_classes = (IsAuthenticated, )

  def update(self, request, *args, **kwargs):
    response = {'message': 'You can\'t update rating like that'}
    return Response(response, status=status.HTTP_400_BAD_REQUEST)

  def create(self, request, *args, **kwargs):
    response = {'message': 'You can\'t create rating like that'}
    return Response(response, status=status.HTTP_400_BAD_REQUEST)
