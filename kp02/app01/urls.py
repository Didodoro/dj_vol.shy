from django.urls import path
from .views import response, response2

urlpatterns = {
    path("",response,name="home"),
    path("text/",response2, name='text'),
}