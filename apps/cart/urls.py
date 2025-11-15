from django.urls import path
from . import views

# namespace so templates can use {% url 'cart:detail' %}
app_name = 'cart'

urlpatterns = [
    path('add/', views.add_to_cart, name='add'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove'),
    path('detail/', views.cart_detail, name='detail'),
]