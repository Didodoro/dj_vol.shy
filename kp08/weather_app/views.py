from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import WeatherData
from datetime import date, timedelta
import random
import pandas as pd
import plotly.express as px

def update_db():
    # Очищення старих даних та генерація 10 нових записів
    WeatherData.objects.all().delete()
    start_date = date.today()
    for i in range(10):
        WeatherData.objects.create(
            date=start_date + timedelta(days=i),
            temperature=round(random.uniform(15, 30), 1),
            pressure=round(random.uniform(700, 800), 1)
        )

def weather_dashboard(request):
    # Обробка AJAX POST-запиту (Оновлення даних)
    if request.method == "POST":
        print(f'if post: request: {request}')
        update_db()
        # Повернення даних у JSON форматі
        new_data = list(WeatherData.objects.all().values().order_by('date'))
        return JsonResponse({'status': 'success', 'data': new_data})
    
    # Формування сторінки при GET-запиті
    print(f'request: {request}')
    update_db()
    data = WeatherData.objects.all().order_by('date')
    df = pd.DataFrame(list(data.values()))
    
    # Створення графіків за допомогою Plotly
    fig_temp = px.line(df, x='date', y='temperature', title="Temperature, °C", markers=True)
    temp_plot = fig_temp.to_html(full_html=False, div_id='temp_plot')
    
    fig_press = px.bar(df, x='date', y='pressure', title="Pressure, mmHg")
    press_plot = fig_press.to_html(full_html=False, div_id='press_plot')
    
    return render(request, 'dashboard.html', {
        'data': data,
        'temp_plot': temp_plot,
        'press_plot': press_plot
    })