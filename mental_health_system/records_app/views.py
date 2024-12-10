from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Product, Order, OrderItem

# Customer Views
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})

def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    orders = Order.objects.filter(customer=customer)
    return render(request, 'customers/customer_detail.html', {'customer': customer, 'orders': orders})

# Product Views
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

# Order Views
def order_list(request):
    orders = Order.objects.select_related('customer').all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'orders/order_detail.html', {'order': order, 'order_items': order_items})
