# shop/admin.py

# Django modules
from django.contrib import admin

# Locals
from shop import models 

# Register your models here.

@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
	list_display = ['slider_title', 'created']

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category_name', 'category_slug']
	prepopulated_fields = {'category_slug':('category_name',)}

@admin.register(models.SubCategory)
class SubcategoryAdmin(admin.ModelAdmin):
	list_display = ['subcategory_name', 'subcategory_slug']
	prepopulated_fields = {'subcategory_slug':('subcategory_name',)}

@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
	list_display = ['brand_name', 'brand_slug']
	prepopulated_fields = {'brand_slug':('brand_name',)}

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['product_name', 'product_slug', 
		'product_image', 'product_price', 'is_available', 
		'created', 'updated']
	list_filter = ['is_available', 'created', 'updated']
	list_editable = ['product_price', 'is_available']
	prepopulated_fields = {'product_slug': ('product_name',)}

