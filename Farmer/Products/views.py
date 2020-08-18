from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


def additem(request, id1):
    p1 = '/cart/item_increment/'+str(id1)
    return HttpResponseRedirect(p1)


def homepage(request):
    username = None
    if request.user.is_authenticated:
        product = Product.objects.all()
        username = request.user.username
        return render(request, 'index.html', {'product': product, 'username': username})
    else:
        return HttpResponseRedirect('login/')


@login_required(login_url="/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/")


@login_required(login_url="/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

@login_required(login_url="/login")
def item_increment1(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add1(product=product)
    return redirect("cart_detail")

@login_required(login_url="/login")
def item_increment10(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add10(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

@login_required(login_url="/login")
def item_decrement1(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement1(product=product)
    return redirect("cart_detail")

@login_required(login_url="/login")
def item_decrement10(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement10(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_detail(request):
    cart = Cart(request)
    p = cart.total()
    return render(request, 'cart/cart_detail.html', {'p': p})
