from django import forms

class WeatherGeneratorForm(forms.Form):
    # Поля для температури [cite: 365, 370]
    min_temp = forms.FloatField(initial=10.0, label='Мін. температура (°C)', 
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
    max_temp = forms.FloatField(initial=30.0, label='Макс. температура (°C)', 
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    # Межі для тиску [cite: 613]
    min_press = forms.FloatField(initial=700.0, label='Мін. тиск (мм рт.ст.)', 
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}))
    max_press = forms.FloatField(initial=800.0, label='Макс. тиск (мм рт.ст.)', 
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    # Межі для вологості та вітру [cite: 613]
    min_humid = forms.FloatField(initial=30.0, label='Мін. вологість (%)', 
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}))
    max_humid = forms.FloatField(initial=90.0, label='Макс. вологість (%)', 
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    min_wind = forms.FloatField(initial=0.0, label='Мін. швидкість вітру (м/с)', 
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
    max_wind = forms.FloatField(initial=15.0, label='Макс. швидкість вітру (м/с)', 
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    # Кількість днів для вимірювань [cite: 613]
    days_count = forms.IntegerField(initial=10, label='Кількість днів', 
                                    widget=forms.NumberInput(attrs={'class': 'form-control'}))