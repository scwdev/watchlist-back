from .models import Movies
from rest_framework import viewsets, permissions
from .serializer import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Movies.objects.all()
    # The serializer class for serializing output
    serializer_class = MovieSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]