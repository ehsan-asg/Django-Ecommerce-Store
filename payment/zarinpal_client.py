import requests
import json
from django.conf import settings

class ZarinPalSandbox:
    _payment_request_url = "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
    _payment_verify_url = "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
    _payment_page_url = "https://sandbox.zarinpal.com/pg/StartPay/"
    
    _domain = getattr(settings, 'MY_SITE_DOMAIN', 'example.com')
    _protocol = getattr(settings, 'MY_SITE_PROTOCOL', 'https')
    _callback_url = f"{_protocol}://{_domain}/payment/verify"

    def __init__(self, merchant_id="test"):
        self.merchant_id = merchant_id

    def payment_request(self, amount, description="پرداختی کاربر"):
        payload = {
            "MerchantID": self.merchant_id,
            "Amount": str(amount),
            "CallbackURL": self._callback_url,
            "Description": description,
        }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(
            self._payment_request_url, headers=headers, data=json.dumps(payload))

        return response.json()

    def payment_verify(self, amount, authority):
        payload = {
            "MerchantID": self.merchant_id,
            "Amount": amount,
            "Authority": authority
        }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(self._payment_verify_url, headers=headers, data=json.dumps(payload))
        return response.json()

    def generate_payment_url(self, authority):
        return f"{self._payment_page_url}{authority}"
