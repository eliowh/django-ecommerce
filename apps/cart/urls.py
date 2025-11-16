from django.urls import path
from . import views   # <-- note the dot

app_name = 'cart'

urlpatterns = [
    # /cart/  → cart_detail page
    path('', views.cart_detail, name='cart_detail'),

    # /cart/add/  → add to cart
    path('add/', views.add_to_cart, name='add'),

    # /cart/remove/123/  → remove item with id 123
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove'),
]