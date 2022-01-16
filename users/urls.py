# users/urls.py

# Django modules
from django.urls import path

# Django locals
from users import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
