from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email, password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    # def test_new_user_email_normalized(self):
    #     """Test the email for new user is normalized"""
    #     email = "test@GMAIL.COM"
    #     user = get_user_model().objects.create(email, 'test123')
    #     self.assertEqual(user.email, email.lower())

    def test_new_user_email_domain_normalized(self):
        """Test the email domain for a new user is normalized but the id left intact"""
        email_identifier = 'TeSt'
        email_domain = 'GMAIL.COM'
        email = f'{email_identifier}@{email_domain}'
        user = get_user_model().objects.create_user(email, 'test123')
        email_domain_lower = email_domain.lower()
        self.assertEqual(user.email, f'{email_identifier}@{email_domain_lower}')

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        # what this does is anything that we run in here should raise the ValueError, and if it doesn't raise a ValueEror, then this test will fail
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com', 'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

