from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id','name','model','engine_type','transmission','horse_power','cylinders','car_image']