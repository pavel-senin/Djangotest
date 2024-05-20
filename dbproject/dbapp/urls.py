# urls.py
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('clients/', client_list, name='client_list'),
    path('clients/<int:client_id>/', client_detail, name='client_detail'),
    
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    
    path('orders/', order_list, name='order_list'),
    path('orders/<int:order_id>/', order_detail, name='order_detail'),

    path('<int:user_id>/ordered_products/', ordered_products, name='ordered_products'),
]

