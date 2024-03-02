from rest_framework.test import APITestCase
from user.serializers import UserSerializer

class UserSerializerTestCase(APITestCase):
    #  Test case for valid data
    def test_user_serialzier_valid_data(self):
        data = {
            'email': 'test@gmail.com',
            'username': 'test',
            'password': 'testHello1'
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors,{})

    def test_validate(self):
        data = {'password': 'test'}

        self.assertTrue(len(data['password'])<6)
        self.assertTrue({'error': 'Password length should be at least 6.'})

    def test_validate(self):
        data = {'password': 'testest'}
        password = data['password']
        self.assertTrue(not any(p.isupper() for p in password))
        self.assertTrue({'error': 'Password must contain at least 1 upper letter.'})

    def test_validate(self):
        data = {'password': 'testest'}
        password = data['password']
        self.assertTrue(not any(p.isdigit() for p in password))
        self.assertTrue({'error': 'Password must contain at least 1 digit.'})
    # Test case for user serializers endhere >>>>>>>
        


        




