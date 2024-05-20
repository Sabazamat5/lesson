from django.db import models

# Create your models here.
from django_countries.fields import CountryField

from django_countries import countries

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo/tournament/',blank=True)
    country = CountryField()
