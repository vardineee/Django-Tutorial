from django.db import models

# Create your models here.

class Passenger(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    rewardPoints = models.FloatField()

    def __str__(self):
        return self.email
