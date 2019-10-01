from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, API Client
from rest_framework.views import status
from .models import Beer, Brewery, Tag, Style, Location
from .serializers import BeerSerializer

# Tests for views

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_beer(beer_name="", ibu="", abv="", description="", brewery_name="", tag_name="", style_basic="", style_detailed="", city="", country="")
        if name != "" and ibu != "" and abv != "" and description != "":
            location = Location(city=city, country=country)
            location.save()
            brewery = Brewery(name=brewery_name, location=location)
            brewery.save()
            tag = Tag(name=tag_name)
            tag.save()
            style = Style(basic=style_basic, detailed=style_detailed)
            style.save()
            beer = Beer(name=beer_name, ibu=ibu, abv=abv, description=description, brewery=brewery, style=style)
            beer.tags_set.add(tag)
            beer.save()

    def setup(self):
        # add test data
        self.create_beer("Revalation Stout", 12, 5.5, "Tasty beer stuff!", "Rock Bridge Brewery", "Chocolately", "Stout", "Bavarian Stout", "New York", "USA")
        self.create_beer("Firestone Jack Double IPA", 54, 8.92, "Bitter IPA stuff", "4 Hands Brewing", "Hoppy", "IPA", "Double IPA", "Wooldridge", "USA")
        self.create_beer("Snake Oil", 32, 3.6, "Smooth and malty", "Civil Life", "Dangerous", "Brown Ale", "American Brown", "Newport", "USA")
        self.create_beer("Budwieser", 3, 4.5, "refreshing classic", "Anheisur Busch", "refreshing", "Lager", "American Lager", "St. Louis", "USA")

class GetAllBeersTest(BaseViewTest):
    """
    This test ensures that all the beers added in the setup method
    exist when we make a GET request to the beers/ endpoint
    """
    def test_get_all_beers(self):
    # hit the API endpoint
    response = self.client.get(
        reverse("beers", kwargs={"version":"v1"})
    )

    # fetch the data from db
    expected = Beer.objects.all()
    serialized = BeerSerializer(expected, many=True)
    self.assertEqual(response.data, serialized.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
