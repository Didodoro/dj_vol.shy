from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    text = models.TextField()
    data = models.DateField(default=timezone.now)
    temperature = models.FloatField()
    pressure = models.FloatField()
    wind_speed = models.FloatField()
    dosh = models.FloatField()

class PostAdmin(admin.ModelAdmin):
    list_display = ["text","data","temperature","pressure","wind_speed","dosh"]
