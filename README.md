# 2022-django-eshopper
Based on CodingEx tutorial on Youtube


#### 1. Basics setup: project, app, static and media files and template and home page

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        ...
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py
        new file:   shop/__init__.py
        new file:   shop/admin.py
        new file:   shop/apps.py
        new file:   shop/migrations/__init__.py
        new file:   shop/models.py
        new file:   shop/tests.py
        new file:   shop/urls.py
        new file:   shop/views.py
        new file:   templates/index.html


#### 2. Create base template and modified navbar

        modified:   README.md
        new file:   templates/base.html
        modified:   templates/index.html


#### 3. Create products page

        modified:   shop/urls.py
        modified:   shop/views.py
        modified:   templates/base.html
        new file:   templates/products.html


#### 4. Create product_detail page

        modified:   shop/urls.py
        modified:   shop/views.py
        modified:   templates/index.html
        new file:   templates/product_detail.html
        modified:   templates/products.html


#### 5. Create contact page

        modified:   README.md
        modified:   shop/urls.py
        modified:   shop/views.py
        modified:   templates/base.html
        new file:   templates/contact.html


#### 6. Create blog app and posts page

        new file:   blog/__init__.py
        new file:   blog/admin.py
        new file:   blog/apps.py
        new file:   blog/migrations/__init__.py
        new file:   blog/models.py
        new file:   blog/tests.py
        new file:   blog/urls.py
        new file:   blog/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   templates/base.html
        new file:   templates/posts.html


#### 7. Create post_detail page 

        modified:   blog/urls.py
        modified:   blog/views.py
        new file:   templates/post_detail.html
        modified:   templates/posts.html


#### 8. Create users app, and register_login page


        modified:   config/settings.py
        modified:   config/urls.py
        modified:   shop/urls.py
        modified:   shop/views.py
        modified:   templates/base.html
        new file:   templates/cart.html
        modified:   templates/products.html
        new file:   templates/register_login.html
        new file:   users/__init__.py
        new file:   users/admin.py
        new file:   users/apps.py
        new file:   users/migrations/__init__.py
        new file:   users/models.py
        new file:   users/tests.py
        new file:   users/urls.py
        new file:   users/views.py


#### ================== END STATIC APP ========================


#### 9. Creare model for Category, SubCategory and Product

        modified:   README.md
        new file:   media/products/2022/01/15/product1.jpg
        new file:   media/products/2022/01/15/product2.jpg
        new file:   media/products/2022/01/15/product4.jpg
        new file:   media/products/2022/01/15/product5.jpg
        new file:   media/products/2022/01/15/product6.jpg
        modified:   shop/admin.py
        new file:   shop/migrations/0001_initial.py
        new file:   shop/migrations/0002_auto_20220115_0736.py
        new file:   shop/migrations/0003_auto_20220115_0739.py
        modified:   shop/models.py































































































