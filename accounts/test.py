from django.test import TestCase
from .models import User


class TestUserModel(TestCase):

    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'phone_number': '12345678901',
            'full_name': 'Test User',
            'role': 'User',
            'image_profile': 'path/to/image.jpg',
            'is_active': True,
            'is_admin': False,
        }

    def test_create_user(self):
        user = User.objects.create(**self.user_data)
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, self.user_data['email'])
        self.assertEqual(user.phone_number, self.user_data['phone_number'])
        self.assertEqual(user.full_name, self.user_data['full_name'])
        self.assertEqual(user.role, self.user_data['role'])
        self.assertEqual(user.image_profile, self.user_data['image_profile'])
        self.assertEqual(user.is_active, self.user_data['is_active'])
        self.assertEqual(user.is_admin, self.user_data['is_admin'])

    def test_user_str_method(self):
        user = User.objects.create(**self.user_data)
        self.assertEqual(str(user), self.user_data['email'])