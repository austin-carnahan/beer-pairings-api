from django.contrib import admin
from .models import Location, Brewery, Style, Tag, Beer, Food, Pairing
# Register your models here.

admin.site.register(Location)
admin.site.register(Brewery)
admin.site.register(Style)
admin.site.register(Tag)
admin.site.register(Beer)
admin.site.register(Food)
admin.site.register(Pairing)
