from django.test import TestCase
from .models import Order

class OrderModelTest(TestCase):

    def setUp(self):
        self.order = Order.objects.create(
            # Add necessary fields for the Order model
            # Example: user=user_instance, total_amount=100.00
        )

    def test_order_creation(self):
        self.assertIsInstance(self.order, Order)
        self.assertEqual(str(self.order), 'Expected string representation of the order')

    def test_order_total_amount(self):
        self.assertEqual(self.order.total_amount, 100.00)  # Replace with the expected total amount

    # Add more tests as needed for other functionalities of the Order model