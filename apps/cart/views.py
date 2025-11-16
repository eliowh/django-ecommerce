from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Cart, CartItem
from apps.products.models import Product
from django.contrib.auth.decorators import login_required

def merge_session_cart_to_user_cart(request, user):
    """Merge anonymous session cart with user's database cart when they log in"""
    session_cart = request.session.get('cart', {})
    
    if session_cart:
        # Get or create user's cart
        cart, created = Cart.objects.get_or_create(user=user)
        
        for product_id, quantity in session_cart.items():
            try:
                product = Product.objects.get(id=product_id)
                cart_item, created = CartItem.objects.get_or_create(
                    cart=cart, 
                    product=product,
                    defaults={'quantity': quantity}
                )
                
                if not created:
                    # If item already exists, add the quantities
                    cart_item.quantity += quantity
                    cart_item.save()
                    
            except Product.DoesNotExist:
                continue
        
        # Clear the session cart after merging
        request.session['cart'] = {}
        request.session.modified = True

def cart_detail(request):
    """Show cart details for both authenticated and anonymous users"""
    if request.user.is_authenticated:
        # For logged-in users, use database cart
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        cart_total = sum(item.quantity * item.product.price for item in cart_items)
    else:
        # For anonymous users, use session-based cart
        session_cart = request.session.get('cart', {})
        cart_items = []
        cart_total = 0
        
        for product_id, quantity in session_cart.items():
            try:
                product = Product.objects.get(id=product_id)
                item_total = product.price * quantity
                cart_items.append({
                    'product': product,
                    'quantity': quantity,
                    'total_price': item_total
                })
                cart_total += item_total
            except Product.DoesNotExist:
                continue
        
        cart = None  # No cart object for anonymous users
    
    return render(request, 'cart/detail.html', {
        'cart': cart,
        'cart_items': cart_items,
        'cart_total': cart_total,
        'is_authenticated': request.user.is_authenticated
    })

def add_to_cart(request, product_id):
    """Add product to cart for both authenticated and anonymous users"""
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity', 1))
        except (ValueError, TypeError):
            messages.error(request, 'Invalid quantity. Please enter a valid number.')
            return redirect('products:list')
        
        product = get_object_or_404(Product, id=product_id)
        
        # Validate quantity
        if quantity < 1:
            messages.error(request, 'Quantity must be at least 1.')
            return redirect('products:list')
        
        if quantity > product.stock:
            messages.error(request, f'Only {product.stock} items available in stock for {product.name}.')
            return redirect('products:list')
        
        if quantity > 999:
            messages.error(request, 'Maximum quantity per item is 999.')
            return redirect('products:list')
        
        if request.user.is_authenticated:
            # For logged-in users, use database cart
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            
            if created:
                cart_item.quantity = quantity
            else:
                cart_item.quantity += quantity
            cart_item.save()
        else:
            # For anonymous users, use session cart
            session_cart = request.session.get('cart', {})
            product_id_str = str(product_id)
            
            if product_id_str in session_cart:
                session_cart[product_id_str] += quantity
            else:
                session_cart[product_id_str] = quantity
            
            request.session['cart'] = session_cart
            request.session.modified = True
        
        messages.success(request, f'Added {quantity} x {product.name} to your cart!')
        return redirect('products:list')
    return redirect('products:list')

def remove_from_cart(request, item_id):
    """Remove items from cart for both authenticated and anonymous users"""
    if request.user.is_authenticated:
        # For logged-in users, remove from database
        try:
            cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
            cart_item.delete()
        except CartItem.DoesNotExist:
            pass
    else:
        # For anonymous users, remove from session
        # item_id in this case would be the product_id
        session_cart = request.session.get('cart', {})
        if str(item_id) in session_cart:
            del session_cart[str(item_id)]
            request.session['cart'] = session_cart
            request.session.modified = True
    
    return redirect('cart:detail')

@login_required
def update_cart_item(request, product_id):
    """Update cart item quantities (only for authenticated users)"""
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(cart=cart, product__id=product_id)
    quantity = request.POST.get('quantity')
    cart_item.quantity = quantity
    cart_item.save()
    return JsonResponse({'success': True})