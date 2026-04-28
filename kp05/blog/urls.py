from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView # Імпортуйте нове представлення

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'), # Новий шлях
]