from django.test import TestCase
from .models import Payment

class PaymentModelTest(TestCase):
    def setUp(self):
        self.payment = Payment.objects.create(
            amount=100.00,
            currency='USD',
            status='completed'
        )

    def test_payment_creation(self):
        self.assertEqual(self.payment.amount, 100.00)
        self.assertEqual(self.payment.currency, 'USD')
        self.assertEqual(self.payment.status, 'completed')

    def test_payment_str(self):
        self.assertEqual(str(self.payment), f"{self.payment.amount} {self.payment.currency} - {self.payment.status}")