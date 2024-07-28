from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('equipment/', views.equipment_list, name='equipment_list'),
    path('equipment/<int:pk>/', views.equipment_detail, name='equipment_detail'),
    path('equipment/add/', views.add_equipment, name='add_equipment'),
    path('equipment/<int:pk>/edit/', views.edit_equipment, name='edit_equipment'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:pk>/edit/', views.edit_user, name='edit_user'),
    path('order_history/', views.order_history, name='order_history'),
    
]
