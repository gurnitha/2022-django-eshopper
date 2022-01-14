# users/urls.py

# Django modules
from django.urls import path

# Django locals
from users import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
