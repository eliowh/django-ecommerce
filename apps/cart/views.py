from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Cart, CartItem
from products.models import Product

def cart_detail(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'cart/detail.html', {'cart': cart})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:cart_detail')

def remove_from_cart(request, product_id):
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(cart=cart, product__id=product_id)
    cart_item.delete()
    return redirect('cart:cart_detail')

def update_cart_item(request, product_id):
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(cart=cart, product__id=product_id)
    quantity = request.POST.get('quantity')
    cart_item.quantity = quantity
    cart_item.save()
    return JsonResponse({'success': True})