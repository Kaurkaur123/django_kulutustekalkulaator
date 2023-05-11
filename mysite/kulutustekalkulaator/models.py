from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Sisestatav(models.Model):
    võlgneja = models.CharField(max_length=100)
    makstav = models.CharField(max_length=100)
    väärtus = models.IntegerField(default=0)
    kirjeldus = models.CharField(max_length=200)
    def __str__(self):
        return self.võlgneja

class Tulemus(models.Model):
    nimi =  models.CharField(max_length=100)
    väärtus = models.IntegerField(default=0)

volgneja = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
