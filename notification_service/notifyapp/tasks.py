from celery import shared_task
import random

@shared_task
def send_otp_via_sms(phone_number):
    otp = random.randint(100000, 999999)
    # This is a dummy function simulating sending SMS
    sms_provider_send(phone_number, otp)
    return otp

def sms_provider_send(phone_number, otp):
    # Simulate an API call to an SMS provider
    print(f"Sending OTP {otp} to phone number {phone_number}")