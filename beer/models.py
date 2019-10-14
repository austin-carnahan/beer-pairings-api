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
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Style(models.Model):
    basic = models.CharField(max_length=60, blank=False)
    detailed = models.CharField(max_length=80, blank=True)

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
    ]
    
    name = models.CharField(max_length=80, blank=False)
    abv = models.FloatField(blank=True, null=True)
    ibu = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=False)
    limited_release = models.BooleanField(null=True, default=None)
    seasonal_release = models.BooleanField(null=True, default=None)
    season = models.CharField(max_length=2, choices= SEASON_CHOICES, blank=True) 
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    sighting = models.ManyToManyField(Location, related_name='sightings')
    tags = models.ManyToManyField(Tag)
    pairings = models.ManyToManyField(Food, through='Pairing')

    def __str__(self):
        return self.name

class Pairing(models.Model):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE) 
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.food + " with " + self.beer

