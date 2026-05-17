import random
import pandas as pd
import plotly.express as px
from django.shortcuts import render, redirect
from .models import WeatherData
from .forms import WeatherGeneratorForm
from datetime import date, timedelta

def weather_dashboard(request):
    # Завдання 2.1: Генерація при кожному завантаженні або через POST
    if request.method == "POST":
        form = WeatherGeneratorForm(request.POST)
    else:
        # Для автоматичної генерації при першому вході використовуємо значення за замовчуванням 
        form = WeatherGeneratorForm()

    if form.is_valid() or request.method == "GET":
        # Отримання даних із форми або використання початкових значень 
        cleaned_data = form.cleaned_data if form.is_valid() else {field: form[field].field.initial for field in form.fields}
        
        # Очищення бази та генерація нових даних 
        WeatherData.objects.all().delete()
        start_date = date.today()
        
        for i in range(cleaned_data['days_count']):
            WeatherData.objects.create(
                date=start_date + timedelta(days=i),
                temperature=round(random.uniform(cleaned_data['min_temp'], cleaned_data['max_temp']), 1),
                pressure=round(random.uniform(cleaned_data['min_press'], cleaned_data['max_press']), 1),
                humidity=round(random.uniform(cleaned_data['min_humid'], cleaned_data['max_humid']), 1),
                wind_speed=round(random.uniform(cleaned_data['min_wind'], cleaned_data['max_wind']), 1)
            )
        
        # Якщо це був POST, перенаправляємо на GET для відображення 
        if request.method == "POST":
            return redirect('weather_dashboard')

    # Отримання даних для графіків 
    data = WeatherData.objects.all().order_by('date')
    df = pd.DataFrame(list(data.values()))

    plots = {}
    if not df.empty:
        # Температура [cite: 449, 452]
        plots['temp_plot'] = px.line(df, x='date', y='temperature', title="Temperature, °C", markers=True).to_html(full_html=False)
        # Тиск [cite: 458, 460]
        plots['press_plot'] = px.bar(df, x='date', y='pressure', title="Pressure, mmHg").to_html(full_html=False)
        # Вологість та вітер (завдання з КП07, актуальні для КП08) [cite: 262]
        plots['humid_plot'] = px.line(df, x='date', y='humidity', title="Humidity, %").to_html(full_html=False)
        plots['wind_plot'] = px.bar(df, x='date', y='wind_speed', title="Wind Speed, m/s").to_html(full_html=False)

    return render(request, 'dashboard.html', {'data': data, 'form': form, **plots})