import random
import pandas as pd
import plotly.express as px
from django.shortcuts import render
from .models import WeatherData
from datetime import date, timedelta

def weather_dashboard(request):
    # Завдання 2.1: Генеруємо дані при кожному завантаженні 
    WeatherData.objects.all().delete()
    start_date = date.today()
    for i in range(10):
        WeatherData.objects.create(
            date=start_date + timedelta(days=i),
            temperature=round(random.uniform(15, 30), 1),
            pressure=round(random.uniform(700, 800), 1),
            humidity=round(random.uniform(30, 90), 1),      
            wind_speed=round(random.uniform(0, 15), 1)      
        )

    data = WeatherData.objects.all().order_by('date')
    df = pd.DataFrame(list(data.values()))

    # Створення графіків [cite: 132]
    temp_plot = px.line(df, x='date', y='temperature', title="Temperature Trend, °C", markers=True).to_html(full_html=False)
    press_plot = px.bar(df, x='date', y='pressure', title="Pressure Trend, mmHg").to_html(full_html=False)
    
    # Нові графіки для завдання 2.2 
    humid_plot = px.line(df, x='date', y='humidity', title="Humidity Trend, %").to_html(full_html=False)
    wind_plot = px.bar(df, x='date', y='wind_speed', title="Wind Speed Trend, m/s").to_html(full_html=False)

    return render(request, 'dashboard.html', {
        'data': data,
        'temp_plot': temp_plot,
        'press_plot': press_plot,
        'humid_plot': humid_plot,
        'wind_plot': wind_plot
    })