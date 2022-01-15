# shop/views.py

# Django modules
from django.shortcuts import render

# Locals
from shop import models

# Create your views here.

def index(request):

	# Grab all category objects
	category_list = models.Category.objects.all()

	# Grab all featured products
	featured_product_list = models.Product.objects.filter(is_featured=True)

	# Put objects in context dictionary
	context = {
		'category_list':category_list,
		'featured_product_list':featured_product_list,
	}
	
	# Fetch context into the template
	return render(request, 'index.html', context)


def products(request):
	return render(request, 'products.html')


def product_detail(request):
	return render(request, 'product_detail.html')


def cart(request):
	return render(request, 'cart.html')


def contact(request):
	return render(request, 'contact.html')
