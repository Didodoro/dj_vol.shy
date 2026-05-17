from django.db import models

class WeatherData(models.Model):
    date = models.DateField()
    temperature = models.FloatField()  
    pressure = models.FloatField()     
    humidity = models.FloatField()     
    wind_speed = models.FloatField()   