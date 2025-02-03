from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),  # ✅ Новый маршрут
    path('logout/', views.user_logout, name='logout'),
]
