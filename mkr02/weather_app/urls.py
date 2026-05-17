from django.urls import path
from . import views

urlpatterns = [
    # Маршрут для головної сторінки дашборду
    path('', views.weather_dashboard, name='weather_dashboard'),
]