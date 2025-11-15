from django.urls import path
from . import views

# Expose payment/checkout URLs under the 'checkout' namespace so templates can
# use `{% url 'checkout:checkout' %}` and related names.
app_name = 'checkout'

urlpatterns = [
    # root of the checkout app shows the checkout page (GET) and processes POST
    path('', views.process_payment, name='checkout'),
    path('process/', views.process_payment, name='process_payment'),
    path('success/', views.payment_success, name='payment_success'),
    path('failure/', views.payment_failure, name='payment_failure'),
]