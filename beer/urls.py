from django.urls import path
from .views import ListBeersView

urlpatterns = [
    path('beers/', ListBeersView.as_view(), name="beers-all")
]
