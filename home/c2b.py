import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth


class C2B:
    consumer_key = settings.CONSUMER_KEY
    consumer_secret = settings.CONSUMER_SECRET
    api_url = settings.API_URL
    payment_url = settings.PAYMENT_URL

    def access_token(self):
        r = requests.get(self.api_url, auth=HTTPBasicAuth(
            self.consumer_key, self.consumer_secret))
        access_token = r.json()["access_token"]
        return access_token

    def register_url(self, access_token):
        register_url = settings.REGISTER_URL
        headers = {
            "Authorization": "Bearer %s" % access_token,
            "Content-Type": "application/json"
        }
        body = {
            "ShortCode": settings.SHORT_CODE,
            "ResponseType": "Completed",
            "ConfirmationURL": settings.CONFIRMATION_URL,
            "ValidationURL": settings.VALIDATION_URL
        }
        r = requests.post(register_url, json=body, headers=headers)

        return r

    def request_payment(self, access_token, amount, phone_number):
        headers = {
            "Authorization": "Bearer %s" % access_token,
            "Content-Type": "application/json"
        }
        body = {
            "ShortCode": settings.SHORT_CODE,
            "CommandID": "CustomerPayBillOnline",
            "Amount": amount,
            "Msisdn": phone_number,
            "BillRefNumber": "High Chance Tips"
        }
        print('-----------Customer Making Payment----------')
        r = requests.post(self.payment_url, json=body, headers=headers)
        return r

    def validate_payment(self, response):
        amount = response["TransAmount"]

        accepted = {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
        rejected = {
            "ResultCode": 1,
            "ResultDesc": "Rejected"
        }
        print('-----------Validating Payment----------')
        return [rejected, accepted][amount == "100"]

    def confirm_payment(self, response):
        amount = response["TransAmount"]
        success = {
            "C2BPaymentConfirmationResult": "Success"
        }
        failed = {
            "C2BPaymentConfirmationResult": "Failed"
        }
        print('-----------Confirming Payment----------')
        return [failed, success][amount == "100"]
