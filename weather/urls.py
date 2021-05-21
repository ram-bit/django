from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('searchcity/', views.index, name='index2'),
    path('whatsWeather/', views.weather, name='weather'),
    path('searchcity/weather/', views.fillweather)
]