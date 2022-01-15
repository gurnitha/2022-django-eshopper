# shop/views.py

# Django modules
from django.shortcuts import render

# Locals
from shop import models

# Create your views here.

def index(request):

	# # Grab all category objects
	# category_list = models.Category.objects.all()

	# # LOAD FEATURED PRODUCTS BASED ON ITS CATEGORY AND SUBCATEGORY

	# # 1. Get category id
	# category_id = request.GET.get('category')
	# # 2. Get all products based on its category and subcategory
	# if category_id:
	# 	featured_product_list = models.Product.objects.filter(subcategory_id=category_id, is_featured=True).order_by('-id')[0:1]
	# # 3. Otherwise grab all products
	# else:
	# 	featured_product_list = models.Product.objects.filter(is_featured=True)

	# # Put objects in context dictionary
	# context = {
	# 	'category_list':category_list,
	# 	'featured_product_list':featured_product_list,
	# }


	'''
		LOAD FEATURED PRODUCTS BASED ON ITS CATEGORY AND SUBCATEGORY
		AND 
		LOAD FEATRUED PRODUCTS BASED ON ITS BRAND
	'''
	
	# 1. Grab all category objects
	category_list = models.Category.objects.all()	

	# 2. Grab all brand objects
	brand_list = models.Brand.objects.all()

	# 3. Get category id from the url
	category_id = request.GET.get('category')
	
	# 3. Get brand id from the url
	brand_id = request.GET.get('brand')

	# 3. Get all products based on its category and subcategory
	if category_id:
		featured_product_list = models.Product.objects.filter(subcategory_id=category_id, is_featured=True).order_by('-id')[0:4]
	# 4. Get all products based on its brand
	elif brand_id:
		featured_product_list = models.Product.objects.filter(brand_id=brand_id, is_featured=True).order_by('-id')[0:4]
	# 5. Otherwise grab all products
	else:
		featured_product_list = models.Product.objects.filter(is_featured=True)

	'''END LOAD ... '''

	product_list = models.Product.objects.all()


	# 6. Put objects in context dictionary
	context = {
		'category_list':category_list,
		'brand_list':brand_list,
		'featured_product_list':featured_product_list,
		'product_list':product_list
	}

	# 7. Fetch context into the template
	return render(request, 'index.html', context)


def products(request):
	return render(request, 'products.html')


def product_detail(request):
	return render(request, 'product_detail.html')


def cart(request):
	return render(request, 'cart.html')


def contact(request):
	return render(request, 'contact.html')
