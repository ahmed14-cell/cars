from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    engine_type = models.CharField(max_length=255)
    transmission = models.CharField(max_length=255)
    horse_power = models.IntegerField()
    cylinders = models.IntegerField()
    car_image = models.ImageField(upload_to = 'vehicles/', default = '')

    def __str__(self):
        return self.name