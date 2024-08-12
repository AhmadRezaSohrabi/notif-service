# notifyapp/views.py
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import send_otp_via_sms
from django.conf import settings

class SendOTPView(APIView):
    def post(self, request):
        # Extract the token from the Authorization header
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return Response({"error": "Authorization token is required"}, status=status.HTTP_401_UNAUTHORIZED)
        
        token = auth_header.split(' ')[1]

        # Verify token with Auth Service
        auth_service_url = f"http://{settings.AUTH_SERVICE_HOST}/auth/verify-token/"
        response = requests.post(auth_service_url, headers={"Authorization": f"Token {token}"})

        if response.status_code != 200:
            return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)

        # Get phone number from request data
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({"error": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Trigger async task to send OTP
        send_otp_via_sms.delay(phone_number)
        return Response({"message": "OTP is being sent to your phone number"}, status=status.HTTP_200_OK)
