from django.test import TestCase
from .models import Cart, CartItem

class CartModelTest(TestCase):

    def setUp(self):
        self.cart = Cart.objects.create()
        self.item1 = CartItem.objects.create(cart=self.cart, product_id=1, quantity=2)
        self.item2 = CartItem.objects.create(cart=self.cart, product_id=2, quantity=1)

    def test_cart_item_count(self):
        self.assertEqual(self.cart.items.count(), 2)

    def test_cart_total_price(self):
        # Assuming product prices are set in the product model
        self.item1.product.price = 10.00
        self.item2.product.price = 20.00
        total_price = self.item1.product.price * self.item1.quantity + self.item2.product.price * self.item2.quantity
        self.assertEqual(self.cart.get_total_price(), total_price)

    def test_cart_item_removal(self):
        self.cart.items.remove(self.item1)
        self.assertEqual(self.cart.items.count(), 1)