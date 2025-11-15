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