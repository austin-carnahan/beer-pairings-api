from django.db import models

class Location(models.Model):
    address1 = models.CharField(max_length=80, blank=True)
    address2 = models.CharField(max_length=80, blank=True)
    address3 = models.CharField(max_length=80, blank=True)
    city = models.CharField(max_length=80, blank=False)
    state = models.CharField(max_length=80, blank=True)
    zipcode = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=80, blank=False)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.city + ", " + self.country

class Brewery(models.Model):
    name = models.CharField(max_length=80, blank=False)
    description = models.Charfield(max_length=200, blank=True)
    shuttered = models.BooleanField(null=True, default=None)
    last_modified = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    website = models.URLField(max_length=120)

    def __str__(self):
        return self.name

class Style(models.Model):
    name = models.CharField(max_length=60, blank=False)
    description = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=60, blank=False)
    description = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=40, blank=False)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=120, blank=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
    
class Beer(models.Model):

    SEASON_CHOICES = [
        ('SP', 'Spring'),
        ('SU', 'Summer'),
        ('FA', 'Fall'),
        ('WI', 'Winter'),
        ('LR', 'Limited release'),
        ('YR', 'Year round'),
        ('RO', 'Rotating'),
    ]
    
    name = models.CharField(max_length=80, blank=False)
    abv = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    ibu = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=False)
    availability = models.CharField(max_length=2, choices= SEASON_CHOICES, blank=True) 
    retired = models.BooleanField(blank=True, Default=None)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sighting = models.ManyToManyField(Location, related_name='sightings', blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    pairings = models.ManyToManyField(Food, through='Pairing', blank=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Pairing(models.Model):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE) 
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.food.name

class Review(models.Model):
    text = models.Charfield(max_length=320, blank=True, default=None)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, default=None)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)

