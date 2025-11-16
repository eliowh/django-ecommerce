from django.urls import path
from . import views   # <-- note the dot

app_name = 'cart'

urlpatterns = [
    # /cart/  → cart_detail page
    path('', views.cart_detail, name='detail'),

    # /cart/add/123/  → add product with id 123 to cart
    path('add/<int:product_id>/', views.add_to_cart, name='add'),

    # /cart/remove/123/  → remove item with id 123
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove'),
]