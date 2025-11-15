from django.shortcuts import render
from django.http import JsonResponse
from .gateway import process_payment as gateway_process_payment


def process_payment(request):
    """View that processes a payment POST and returns JSON response from the gateway."""
    if request.method == 'POST':
        amount = request.POST.get('amount')
        payment_response = gateway_process_payment(amount)
        return JsonResponse(payment_response)
    # GET -> show checkout page
    return render(request, 'checkout/checkout.html')


def payment_success(request):
    return render(request, 'checkout/success.html')


def payment_failure(request):
    return render(request, 'checkout/failure.html')