from django.shortcuts import render
from rest_framework import generics
from .models import Beer
from .serializers import BeerSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ListBeersView(generics.ListAPIView):
    """
    Provides a GET method handler
    """

    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'abv', 'ibu', 'description']
    
