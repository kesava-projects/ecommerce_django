from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Product, Cart


# Create your views here.
def home(request):
    return HttpResponse("Hello, Your on Home Page.")

def add_product(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        stock = request.POST.get('stock')
        category = request.POST.get('category')
        rating = request.POST.get('rating')
        Product.objects.create(id=id, name=name, price=price, description=description, stock = stock,
                               category=category, rating=rating)
        return redirect('http://127.0.0.1:8000/show_products')

    return render(request, "addpro.html")

def show_products(request):
    products = Product.objects.all()
    return render(request, "showpro.html", context={'products': products})

def search_product(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        prod_data = Product.objects.get(id=id)
        return render(request, "searchpro.html", context={'prod_data': prod_data,})
    return render(request, "searchpro.html")

def add_cart(request, id):
    if request.method == 'POST':
        prod = Product.objects.get(id=id)
        id = prod.id
        name = prod.name
        price = prod.price
        Cart.objects.create(prod_id = id, prod_name = name, prod_price=price)
    return redirect('show')

def del_product(request, id):
    prod = Product.objects.get(id=id)
    cart = Cart.objects.get(prod_id=id)
    if cart:
        cart.delete()
    prod.delete()
    return redirect('show')

def edit_product(request, id):
    prod = Product.objects.get(id=id)
    return render(request, "update.html", context = {'prod_data': prod})

def upd_product(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        stock = request.POST.get('stock')
        category = request.POST.get('category')
        rating = request.POST.get('rating')
        prod = Product.objects.get(id=id)
        prod.id = id
        prod.name = name
        prod.price = price
        prod.description = description
        prod.stock = stock
        prod.category = category
        prod.rating = rating
        prod.save()
    return redirect('show')

def show_cart(request):
    carts = Cart.objects.all()
    return render(request, "cart.html", context={'carts': carts})

def delete_from_cart(request, id):
    cart = Cart.objects.get(prod_id=id)
    cart.delete()
    return redirect('cart')

