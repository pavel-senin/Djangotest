# views.py

from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Product, Order, OrderItem
from .forms import *

# Create your views here.


# Client Views
def client_detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client)
    return render(request, 'client_detail.html', {'client': client, 'orders': orders})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

def client_update(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_detail', client_id=client.id)
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form})

def client_delete(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'client_confirm_delete.html', {'client': client})

# Product Views
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    orders = OrderItem.objects.filter(product=product).select_related('order')
    return render(request, 'product_detail.html', {'product': product, 'orders': orders})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})

# Order Views
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

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})

def order_update(request,order_id):
    order = get_object_or_404(Order, id = order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_detail', order_id=order_id)
    else:
        form = OrderForm(instance=order)
    return render(request, 'order_form.html', {'form': form})

def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'order_confirm_delete.html', {'order': order})