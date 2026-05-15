from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

    fields = ['text', 'temperature', 'pressure', 'wind_speed', 'precipitation_prob']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['text', 'temperature', 'pressure', 'wind_speed', 'precipitation_prob']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')