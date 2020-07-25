from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    engine_type = models.CharField(max_length=255)
    transmission = models.CharField(max_length=255)
    horse_power = models.IntegerField()
    cylinders = models.IntegerField()

    def __str__(self):
        return self.name