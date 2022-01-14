# confit/urls.py

# Django modules
from django.urls import path

# Django locals
from shop import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('product/1', views.product_detail, name='product_detail'),
    path('contact/', views.contact, name='contact'),
]
