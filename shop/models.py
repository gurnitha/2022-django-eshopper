# shop/models.py

# Django modules
from django.db import models

# Create your models here.

# Model: Category
class Category(models.Model):
	category_name = models.CharField(max_length=50, db_index=True)
	category_slug = models.SlugField(max_length=100, db_index=True)
	
	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.category_name


# Model: Sub Category
class SubCategory(models.Model):
	subcategory_name = models.CharField(max_length=50)
	subcategory_slug = models.SlugField(max_length=100, db_index=True)
	category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Subcategory'
		verbose_name_plural = 'Subcategories'

	def __str__(self):
		return self.subcategory_name


# Model: Product
class Product(models.Model):
	product_name = models.CharField(max_length=100, db_index=True)
	product_slug = models.SlugField(max_length=100, db_index=True)
	category_id = models.ForeignKey(
					Category, related_name='products', 
					on_delete=models.CASCADE)
	subcategory_id = models.ForeignKey(
					SubCategory, related_name='products', 
					on_delete=models.CASCADE)	
	product_image = models.ImageField(
					upload_to='products/%Y/%m/%d',
					blank=True)
	product_description = models.TextField(blank=True)
	product_price = models.DecimalField(
					max_digits=10, decimal_places=2)
	is_available = models.BooleanField(default=True)
	is_featured = models.BooleanField(default=False)
	is_recomended = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Product'
		verbose_name_plural = 'Products'
		ordering = ('product_name',)
		index_together = (('id', 'product_slug'),)

	def __str__(self):
		return self.product_name
