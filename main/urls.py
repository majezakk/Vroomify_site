from django.urls import path
from . import views
from .views import create_appointment

urlpatterns = [
    path('', views.index, name='index'),
    path('appointment/create/', create_appointment, name='create_appointment'),
]
