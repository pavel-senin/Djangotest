from django import forms
from .models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone_number', 'address']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'date_added', 'image']  # Добавлено поле image

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'status', 'total_amount', 'order_date']