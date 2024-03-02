from django.test import TestCase
from user.models import User
from customer.models import Customer        
from django.test import TestCase
from customer.models import Customer

class UserModelTest(TestCase):
    def test_create_user(self):
        email = 'test@gmail.com'
        username = 'test'
        password = 'testHello1'

        user = User.objects.create_user(username=username,email=email,password=password)
        
        self.assertEqual(user.email,email)
        self.assertEqual(user.username,username)
        self.assertTrue(user.check_password(password))
    
class UserMethodTest(TestCase):
    def test__str__(self):
        user = User(username='test')
        self.assertEqual(user.__str__(),'test')
        

