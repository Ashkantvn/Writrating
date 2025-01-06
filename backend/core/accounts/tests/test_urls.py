from django.test import SimpleTestCase
from django.urls import reverse,resolve
from accounts.api.v1 import views

class TestAccountsUrls(SimpleTestCase):
    def test_profile_is_resolve(self):
        url=reverse('accounts:profile',kwargs={'username':'test'})
        self.assertEqual(resolve(url).func.view_class,views.ProfileAPI)

    def test_sign_up_is_resolve(self):
        url=reverse('accounts:signUp')
        self.assertEqual(resolve(url).func.view_class,views.SignUpAPI)

    def test_sign_up_is_resolve(self):
        url=reverse('accounts:login')
        self.assertEqual(resolve(url).func.view_class,views.LoginAPI)

    def test_sign_up_is_resolve(self):
        url=reverse('accounts:logout')
        self.assertEqual(resolve(url).func.view_class,views.LogoutAPI)    

    def test_sign_up_is_resolve(self):
        url=reverse('accounts:deleteAccount')
        self.assertEqual(resolve(url).func.view_class,views.DeleteAccountAPI)

    def test_sign_up_is_resolve(self):
        url=reverse('accounts:changePass')
        self.assertEqual(resolve(url).func.view_class,views.ChangePassAPI)

    def test_sign_up_is_resolve(self):
        url=reverse('accounts:passwordRecovery')
        self.assertEqual(resolve(url).func.view_class,views.PasswordRecoveryAPI)

    def test_sign_up_is_resolve(self):
        url=reverse('accounts:passwordRecoveryVerification',kwargs={"email":"test@test.com",'code':123})
        self.assertEqual(resolve(url).func.view_class,views.PasswordRecoveryVerificationAPI)