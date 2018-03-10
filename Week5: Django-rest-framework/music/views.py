from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from .models import Artist, Track

class Testing(APIView):
    """Return just a single variable, message, as "hello world!" """
    def get(self, request):
        """Handles get requests."""
        return Response({"message": "hello world!"}, status=status.HTTP_200_OK)
    
    def post(self,request):
        """Handles post reqeusts."""
        return Response({"message":"This was a post request."}, status=status.HTTP_200_OK)

class ArtistDetail(APIView):
    """Returns an artist detail on supplying an id."""
    def post(self, request):
        """Handles get requests."""
        id = request.data['id']
        artist = get_object_or_404(Artist, id=id)
        return Response({"id":artist.id, "name":artist.name, "real_name":artist.real_name})