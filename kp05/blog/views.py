from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView # Додайте цей імпорт
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

# Нове представлення для створення допису
class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    # Вкажіть поля, які користувач має заповнити (без id та date, які заповнюються автоматично)
    fields = ['text', 'temperature', 'pressure', 'wind_speed', 'precipitation_prob']