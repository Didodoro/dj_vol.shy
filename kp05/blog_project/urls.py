from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")), # Вбудовані login/logout
    path("accounts/", include("accounts.urls")), # Ваш signup
    path('', include('blog.urls')),
]