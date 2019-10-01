from django.shortcuts import render
from rest_framework import generics
from .models import Beer
from .serializers import BeerSerializer


class ListBeersView(generics.ListAPIView):
    """
    Provides a GET method handler
    """

    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
