from django.test import TestCase
from .models import Phone,OneTimePassword
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
import json
from .views import PhoneView
from django.conf.urls import  url
from rest_framework.test import APITestCase


# Create your tests here.

class SendOtpTest(APITestCase):
    def setUp(self):
        self.payload={
                        'phone_number':"+2348079895427",
                        'username':"Aderonke"
                    }
        self.client = Client()

    def test_getOtpSent(self):
        response=self.client.get('/refill/otp/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sendOtp(self):

        response=self.client.post('/refill/register/',
                            data=json.dumps(self.payload),
                            content_type='application/json')

        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    

