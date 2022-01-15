# shop/views.py

# Django modules
from django.shortcuts import render

# Locals
from shop import models

# Create your views here.

def index(request):

	# Grab all category objects
	category_list = models.Category.objects.all()


	# LOAD FEATURED PRODUCTS BASED ON ITS CATEGORY AND SUBCATEGORY

	# 1. Get category id
	category_id = request.GET.get('category')
	# 2. Get all products based on its category and subcategory
	if category_id:
		featured_product_list = models.Product.objects.filter(subcategory_id=category_id, is_featured=True)
	# 3. Otherwise grab all products
	else:
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
