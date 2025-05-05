from django.test import TestCase
from django.contrib.auth.models import User
from users.models import Profile
from users.forms import UserRegisterForm
from django.test import RequestFactory
from users.views import CustomLoginView, logout_view
from django.contrib.auth import authenticate
from django.urls import reverse, resolve


#Test cases for models.py
class TestUserModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    #Test profile self function return the correct string name
    def test_profile_str_method(self):
        profile = self.user.profile  #Acces to profile created for test
        expected_str = f'{self.user.username} Profile'
        self.assertEqual(str(profile), expected_str)

    #When creating a user, a profile should be created automatically
    def test_profile_created_signal(self):
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

#Test cases for forms.py
class TestUserForm(TestCase):
    def setUp(self):
        self.form_data = {
            'username': 'newuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'email': 'newuser@example.com',
            'premium': True,
            'location_consent': True
        }
        self.form = UserRegisterForm(data=self.form_data)

    #Register user saves prmium and location_consent fields correctly
    def test_user_register_form_saves_premium(self):
        self.assertTrue(self.form.is_valid())
        user = self.form.save()
        self.assertTrue(user.profile.premium)

    def test_user_register_form_saves_location_consent(self):
        self.assertTrue(self.form.is_valid())
        user = self.form.save()
        self.assertTrue(user.profile.location_consent)

#Test cases for views.py
class TestUserView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    #Verify thath logout_view actually logs out user
    def test_logout_view_logs_out_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('logout'))
        self.assertTemplateUsed(response, 'users/logout.html')
        self.assertEqual(response.status_code, 200)

    #Verify that login is succesfull with correct credentials
    def test_login_successful(self):
        user = authenticate(username='testuser', password='testpass')
        self.assertIsNotNone(user)
        self.assertTrue(user.is_authenticated)

    #Verify that login fails with wrong password
    def test_login_wrong_password(self):
        user = authenticate(username='testuser', password='wrongpass')
        self.assertIsNone(user)

    #Verify that login fails with wrong username as user dont exist
    def test_login_nonexistent_user(self):
        user = authenticate(username='nouser', password='testpass')
        self.assertIsNone(user)

#Test cases for urls.py
class TestUserURL(TestCase):

    #Test that the login and logout URL resolves to the correct view
    def test_login_url_resolves_to_loginview(self):
        view = resolve(reverse('login'))
        self.assertEqual(view.func.view_class, CustomLoginView)

    def test_logout_url_resolves_to_logout_view(self):
        view = resolve(reverse('logout'))
        self.assertEqual(view.func, logout_view)

#Test cases for templates
class TestUserTemplates(TestCase):
    def setUp(self):
      self.user = User.objects.create_user(username='testuser', password='testpass')

    #Verify that the login and logout views use the correct html templates
    def test_login_view_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertEqual(response.status_code, 200)

    def test_logout_view_uses_correct_template(self):
        self.client.force_login(self.user)
        self.assertTrue('_auth_user_id' in self.client.session)
        response = self.client.get(reverse('logout'))
        self.assertTemplateUsed(response, 'users/logout.html')
        self.assertEqual(response.status_code, 200)