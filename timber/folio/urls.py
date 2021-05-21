from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('CV/', views.cv, name='cv'),
    path('contacted/', views.contact, name='contact')
]