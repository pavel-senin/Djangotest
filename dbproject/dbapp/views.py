# views.py

from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render, get_object_or_404
from .models import Client, Product, Order, OrderItem
from django.contrib.auth.decorators import login_required

# Create your views here.



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

def ordered_products(request, user_id):
    client = get_object_or_404(Client, id=user_id)
    orders = Order.objects.filter(client=client)
    context = {
        'client': client,
        'weekly_products': get_ordered_products_within_period(orders, 7),
        'monthly_products': get_ordered_products_within_period(orders, 30),
        'yearly_products': get_ordered_products_within_period(orders, 365),
    }
    return render(request, 'ordered_products.html', context)

def get_ordered_products_within_period(orders, days):
    start_date = timezone.now() - timedelta(days=days)
    ordered_products = set()
    for order in orders.filter(order_date__gte=start_date):
        for item in OrderItem.objects.filter(order=order):
            ordered_products.add(item.product)
    return ordered_products