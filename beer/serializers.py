from rest_framework import serializers
from .models import Beer, Brewery, Style, Tag, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['address1', 'address2', 'address3', 'city', 'state', 'zipcode', 'country', 'lat', 'lon']

class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ['basic', 'detailed']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class BrewerySerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=False)

    class Meta:
        model = Brewery
        fields = ['name', 'location']

class BeerSerializer(serializers.ModelSerializer):
    brewery = BrewerySerializer(many=False)
    style = StyleSerializer(many=False)
    tags = TagSerializer(many=True)

    class Meta:
        model = Beer
        fields = ['name', 'description', 'abv', 'ibu', 'brewery', 'style', 'tags']
