from rest_framework.test import APITestCase,APIClient
from user.models import User
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from rest_framework import status

class Registration(APITestCase):
    def setUp(self):
        pass
    
    def test_registration(self):
        url = reverse('registration')
        data = {
            'email': 'test@gmail.com',
            'username': 'test',
            'password': 'testHello1',
            'group': 1
        }
        response = self.client.post(url, data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'],'test@gmail.com')
        self.assertEqual(response.data['username'],'test')

