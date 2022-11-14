from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=50)
    releaseDate = models.DateField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name 
