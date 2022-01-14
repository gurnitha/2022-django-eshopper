# confit/urls.py

# Django modules
from django.urls import path

# Django locals
from shop import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
]
