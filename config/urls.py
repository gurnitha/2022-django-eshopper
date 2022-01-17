# confit/urls.py

# Django modules
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Django locals

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('', include('blog.urls')),
    path('', include('users.urls')),

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),

    # admin/
    # [name='index']
    # products/ [name='products']
    # product/1 [name='product_detail']
    # cart/ [name='cart']
    # contact/ [name='contact']
    # posts/ [name='posts']
    # post/1 [name='post_detail']
    # signup/ [name='signup']
    # logout/ [name='logout']
    # accounts/ login/ [name='login']
    # accounts/ logout/ [name='logout']
    # accounts/ password_change/ [name='password_change']
    # accounts/ password_change/done/ [name='password_change_done']
    # accounts/ password_reset/ [name='password_reset']
    # accounts/ password_reset/done/ [name='password_reset_done']
    # accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/ reset/done/ [name='password_reset_complete']
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)