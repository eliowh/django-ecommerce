from django.conf import settings
import requests

class PaymentGateway:
    def __init__(self, api_key=None):
        self.api_key = api_key or settings.PAYMENT_GATEWAY_API_KEY
        self.base_url = settings.PAYMENT_GATEWAY_BASE_URL

    def create_payment(self, amount, currency, payment_method, **kwargs):
        url = f"{self.base_url}/payments"
        data = {
            "amount": amount,
            "currency": currency,
            "payment_method": payment_method,
            **kwargs
        }
        response = requests.post(url, json=data, headers=self._get_headers())
        return response.json()

    def get_payment_status(self, payment_id):
        url = f"{self.base_url}/payments/{payment_id}"
        response = requests.get(url, headers=self._get_headers())
        return response.json()

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }


def process_payment(amount, currency='USD', payment_method=None, **kwargs):
    """Compatibility wrapper used by views.py — creates a PaymentGateway and calls create_payment.

    amount is expected to be a numeric or string value acceptable to the gateway.
    """
    gw = PaymentGateway()
    return gw.create_payment(amount=amount, currency=currency, payment_method=payment_method, **kwargs)