from django.shortcuts import render

# Create your views here.


# views.py

from django.shortcuts import render, get_object_or_404
from .models import Client, Product, Order, OrderItem

def client_detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client)
    return render(request, 'client_detail.html', {'client': client, 'orders': orders})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    orders = OrderItem.objects.filter(product=product).select_related('order')
    return render(request, 'product_detail.html', {'product': product, 'orders': orders})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'order_detail.html', {'order': order})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})
