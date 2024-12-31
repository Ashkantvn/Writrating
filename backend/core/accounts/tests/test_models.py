from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models.profile_model import Profile


class TestAccountModels(TestCase):
    def setUp(self):
        self.User = get_user_model()

    # test for user creation
    def test_create_user(self):
        user = self.User.objects.create_user(email="test@test.com",password="waoojfdoiij@3324ADF")
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_validator)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_staff)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            self.User.objects.create_user()
        with self.assertRaises(TypeError):
            self.User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            self.User.objects.create_user(email="",password="asfopahsfi@#4589Sljf")

    # test for create superuser creation
    def test_create_super_user(self):
        user=self.User.objects.create_superuser(email="test@test.com",password="wodojfoadsji@#o5u08ASDF")

        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_admin)
        self.assertTrue(user.is_validator)
        self.assertTrue(user.is_staff)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        with self.assertRaises(ValueError):
            self.User.objects.create_superuser(email='test@test.com',password='pwijsd@#$123SF',is_superuser=False)
        
    # test for create profile model after user creation
    def test_user_create_profile(self):
        user = self.User.objects.create_user(email='test@test.com',password="adjfapwo@#123AFDADS")
        self.assertIsInstance(user.profile,Profile)
        self.assertEqual(user.profile.username,f"user{user.profile.pk}")
        self.assertEqual(user.profile.first_name,"")
        self.assertEqual(user.profile.last_name,"")
        self.assertIsNotNone(user.profile.profile_image)
        self.assertEqual(user.profile.description,"")
        self.assertIsNotNone(user.profile.updated_date)
        self.assertIsNotNone(user.profile.created_date)

    # test for create profile model after superuser creation
    def test_user_create_profile(self):
        user = self.User.objects.create_superuser(email='test@test.com',password="adjfapwo@#123AFDADS")
        self.assertIsInstance(user.profile,Profile)
        self.assertEqual(user.profile.username,f"user{user.profile.pk}")
        self.assertEqual(user.profile.first_name,"")
        self.assertEqual(user.profile.last_name,"")
        self.assertIsNotNone(user.profile.profile_image)
        self.assertEqual(user.profile.description,"")
        self.assertIsNotNone(user.profile.updated_date)
        self.assertIsNotNone(user.profile.created_date)


