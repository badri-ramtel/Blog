from django.urls import path
from auth_app import views

urlpatterns = [
    path('register/', views.user_register, name='authapp-register'),
    path('login/', views.user_login, name='authapp-login'),
    path('logout/', views.user_logout, name='authapp-logout'),
]