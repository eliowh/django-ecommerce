from django.shortcuts import render
from django.http import JsonResponse
from .gateway import process_payment

def payment_view(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        payment_response = process_payment(amount)
        return JsonResponse(payment_response)
    return render(request, 'checkout/checkout.html')