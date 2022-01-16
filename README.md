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

#### ================== DYNAMIC HOME PAGE =====================

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


#### 10. Retrieve and fetch categories

        modified:   README.md
        modified:   shop/views.py
        modified:   templates/index.html


#### 11. Retrieve and fetch subcategories

        modified:   README.md
        modified:   shop/views.py
        modified:   templates/index.html


#### 12. Retrieve and fetch featured products by category and subcategory

        modified:   README.md
        new file:   media/products/2022/01/15/product3.jpg
        modified:   shop/views.py
        modified:   templates/index.html


#### 13. Showing and linking featured product based on category and subcategory 

        modified:   README.md
        new file:   media/products/2022/01/15/gallery1.jpg
        modified:   shop/views.py
        modified:   templates/index.html


#### 14. Showing LIFO for featured products and limit the product to display

        modified:   README.md
        modified:   shop/views.py


#### 15. Create Brand model with OneToMany rel to Product and add some items

        modified:   README.md
        modified:   shop/admin.py
        new file:   shop/migrations/0004_auto_20220115_1447.py
        new file:   shop/migrations/0005_brand_brand_slug.py
        modified:   shop/models.py


#### 16. Retrieve and fetch featured products by brand

        modified:   README.md
        modified:   shop/views.py
        modified:   templates/index.html


#### 17. Retrieve and fetch products by category in accordion tab

        modified:   README.md
        modified:   shop/views.py
        modified:   templates/index.html


#### 18. Displaying redomended products (maximum 6 items) to the home page

        NOTE:

        1. At last, after one full day trying and error making the recomended
           produts slider works, I found my own solution.
        2. My solution might be not the best or the right way, but it works
           for showing maximum 9 items. Each slide contains 3 items.
        3. It you need more items to show 12 items, un-comment the commented codes.
        4. If you want to shoe 15 item, copy the same code, change the number of 
           it to slice, let say, change:
           FROM : slice:"9:12",
           TO   : slice:"12:15",
        5. For now I am :) with my solution.

        modified:   README.md
        modified:   shop/views.py
        modified:   templates/index.html


#### 19. Create Slider model

        modified:   README.md
        new file:   media/sliders/2022/01/16/gallery4.jpg
        new file:   media/sliders/2022/01/16/girl1.jpg
        new file:   media/sliders/2022/01/16/girl2.jpg
        new file:   media/sliders/2022/01/16/girl3.jpg
        modified:   shop/admin.py
        new file:   shop/migrations/0006_slider.py
        modified:   shop/models.py


#### 20. Modify Slider model by adding image_price field, retrieve and fetch sliders

        modified:   README.md
        new file:   media/sliders/2022/01/16/pricing.png
        new file:   media/sliders/2022/01/16/pricing_KQmCo36.png
        new file:   media/sliders/2022/01/16/pricing_pYWSOtt.png
        new file:   media/sliders/2022/01/16/pricing_wzDk2Aa.png
        new file:   shop/migrations/0007_slider_slider_image_price.py
        modified:   shop/models.py
        modified:   shop/views.py
        modified:   templates/index.html


#### ================== END DYNAMIC HOME PAGE =====================

#### ================== USER AUTHENTICATION =======================


#### 21. Create UserCreateForm class 

        modified:   README.md
        modified:   users/models.py
        modified:   users/views.py


#### 22. Move and modify login and signup page

        modified:   README.md
        renamed:    templates/register_login.html -> users/templates/users/login.html
        new file:   users/templates/users/register.html
        modified:   users/views.py

#### 23. SIGN UP 

        NOTE: Sign Up :)

        modified:   README.md
        modified:   users/models.py
        deleted:    users/templates/users/register.html
        renamed:    users/templates/users/login.html -> users/templates/users/registration/login.html
        new file:   users/templates/users/registration/signup.html
        modified:   users/urls.py
        modified:   users/views.py















































































