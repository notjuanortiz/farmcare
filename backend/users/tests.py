from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='basic@user.com', password='test')

        self.assertEqual(user.email, 'basic@user.com')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username does not exist for base user
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='test')

    def test_create_superuser(self):
        User = get_user_model()
        super_user = User.objects.create_superuser(email='super@user.com', password='test')
        self.assertEqual(super_user.email, 'super@user.com')
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
        try:
            self.assertIsNone(super_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='super@user.com', password='test', is_superuser=False)