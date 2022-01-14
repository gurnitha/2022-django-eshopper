# confit/urls.py

# Django modules
from django.urls import path

# Django locals
from blog import views

urlpatterns = [
    path('posts/', views.posts, name='posts'),
]
