from django.db import models
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    temperature = models.FloatField()
    pressure = models.FloatField()
    wind_speed = models.FloatField() # Швидкість вітру
    precipitation_prob = models.FloatField() # Ймовірність опадів

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})