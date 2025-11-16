from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from decimal import Decimal
from apps.cart.models import Cart, CartItem
from apps.products.models import Product
from .gateway import process_payment as gateway_process_payment


def process_payment(request):
    """View that processes a payment POST and creates order confirmation."""
    
    # Calculate cart details first (needed for both GET and POST)
    cart_items = []
    cart_total = Decimal('0')
    
    if request.user.is_authenticated:
        # For logged-in users, get database cart
        try:
            cart = Cart.objects.get(user=request.user)
            cart_items_db = CartItem.objects.filter(cart=cart)
            for item in cart_items_db:
                item_total = item.quantity * item.product.price
                cart_items.append({
                    'product': item.product,
                    'quantity': item.quantity,
                    'price': item.product.price,
                    'total_price': item_total
                })
                cart_total += item_total
        except Cart.DoesNotExist:
            pass
    else:
        # For anonymous users, get session cart
        session_cart = request.session.get('cart', {})
        for product_id_str, quantity in session_cart.items():
            try:
                product = Product.objects.get(id=int(product_id_str))
                item_total = quantity * product.price
                cart_items.append({
                    'product': product,
                    'quantity': quantity,
                    'price': product.price,
                    'total_price': item_total
                })
                cart_total += item_total
            except Product.DoesNotExist:
                continue
    
    # Check if cart is empty
    if not cart_items:
        messages.warning(request, 'Your cart is empty. Add some items before checkout.')
        return redirect('products:list')
    
    # Calculate breakdown (needed for both GET and POST)
    subtotal = Decimal(str(cart_total))
    shipping_fee = Decimal('50.00') if subtotal < Decimal('500') else Decimal('0')  # Free shipping over ₱500
    tax_rate = Decimal('0.12')  # 12% VAT
    tax_amount = subtotal * tax_rate
    total_amount = subtotal + shipping_fee + tax_amount
    
    if request.method == 'POST':
        # Get form data
        payment_method = request.POST.get('payment_method', 'cash_on_delivery')
        
        # Customer details
        customer_name = f"{request.POST.get('first_name', '')} {request.POST.get('last_name', '')}".strip()
        customer_email = request.POST.get('email', '')
        customer_phone = request.POST.get('phone', '')
        
        # Process mock payment
        payment_response = gateway_process_payment(
            amount=str(total_amount),
            payment_method=payment_method,
            customer_name=customer_name,
            customer_email=customer_email
        )
        
        if payment_response['status'] == 'success':
            # Clear the cart after successful order
            if request.user.is_authenticated:
                try:
                    cart = Cart.objects.get(user=request.user)
                    cart.delete()
                except Cart.DoesNotExist:
                    pass
            else:
                # Clear session cart
                request.session['cart'] = {}
            
            # Convert cart items to JSON-serializable format for session storage
            serializable_cart_items = []
            for item in cart_items:
                serializable_cart_items.append({
                    'product': {
                        'id': item['product'].id,
                        'name': item['product'].name,
                        'price': str(item['product'].price),
                        'category': item['product'].category.name if item['product'].category else 'No Category'
                    },
                    'quantity': item['quantity'],
                    'price': str(item['price']),
                    'total_price': str(item['total_price'])
                })
            
            # Store order details in session for success page
            request.session['last_order'] = {
                'transaction_id': payment_response['transaction_id'],
                'receipt_number': payment_response['receipt_number'],
                'amount': str(total_amount),  # Convert Decimal to string
                'payment_method': payment_method,
                'customer_name': customer_name,
                'customer_email': customer_email,
                'timestamp': payment_response['timestamp'],
                'cart_items': serializable_cart_items,  # Use serializable version
                'subtotal': str(subtotal),
                'shipping_fee': str(shipping_fee),
                'tax_amount': str(tax_amount)
            }
            
            messages.success(request, f"Order confirmed! Transaction ID: {payment_response['transaction_id']}")
            return redirect('checkout:payment_success')
        else:
            messages.error(request, 'Order processing failed. Please try again.')
            return redirect('checkout:process_payment')
    
    # GET -> show checkout page with cart details
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping_fee': shipping_fee,
        'tax_amount': tax_amount,
        'tax_rate': tax_rate * 100,  # Convert to percentage
        'total_amount': total_amount,
        'is_authenticated': request.user.is_authenticated,
        'free_shipping_threshold': 500
    }
    
    return render(request, 'checkout/checkout.html', context)


def payment_success(request):
    # Check if there's a recent order
    last_order = request.session.get('last_order', None)
    if not last_order:
        messages.info(request, 'No recent order found.')
        return redirect('products:list')
    
    return render(request, 'checkout/success.html')


def payment_failure(request):
    return render(request, 'checkout/failure.html')