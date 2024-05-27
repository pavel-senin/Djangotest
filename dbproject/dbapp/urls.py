# urls.py
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', client_list, name='client_list'),

    path('clients/', client_list, name='client_list'),
    path('clients/<int:client_id>/', client_detail, name='client_detail'),
    path('clients/create/', client_create, name='client_form'),
    path('clients/<int:client_id>/update/', client_update, name='client_form'),
    path('clients/<int:client_id>/delete/', client_delete, name='client_form_delete'),
    
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('products/create/', product_create, name='product_create'),
    path('products/<int:product_id>/update/', product_update, name='product_update'),
    path('products/<int:product_id>/delete/', product_delete, name='product_delete'),


    path('orders/', order_list, name='order_list'),
    path('orders/<int:order_id>/', order_detail, name='order_detail'),
    path('orders/create/', order_create, name='order_create'),
    path('orders/<int:order_id>/update/', order_update, name='order_update'),
    path('orders/<int:order_id>/delete/', order_delete, name='order_delete'),

    path('<int:user_id>/ordered_products/', ordered_products, name='ordered_products'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
