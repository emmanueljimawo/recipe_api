from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a user with an Email is successful"""
        email = 'test@xyz.com'
        password = 'test'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email of a new user is normalized"""
        email = 'test@XYZ.COM'
        user = get_user_model().objects.create_user(email,'test')

        self.assertEqual(user.email, email.lower())
