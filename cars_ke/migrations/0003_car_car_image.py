# Generated by Django 3.0.8 on 2020-07-25 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_ke', '0002_auto_20200725_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_image',
            field=models.ImageField(default='', upload_to='cars/'),
        ),
    ]
