from django.test import TestCase
from .models import User  # Assuming you have a User model in models.py

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('password123'))

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_user_email(self):
        self.assertEqual(self.user.email, 'testuser@example.com')