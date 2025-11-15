from django.urls import path, include

urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('products/', include('apps.products.urls')),
    path('orders/', include('apps.orders.urls')),
    path('cart/', include('apps.cart.urls')),
    path('payments/', include('apps.payments.urls')),
]