from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import reverse
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm



# Forms

# class TestUserRegistrationForm(TestCase):
#     def test_registration_valid(self):
#             form = UserRegisterForm({'username':"testuser",
#                                          "email": "test@example.com",
#                                          "password1": "test_password",
#                                          "password2": "test_password",
#                                          })
#             self.assertTrue(form.is_valid())
            
#     def test_passwords_do_not_match(self):
#         form = UserRegisterForm({"username": "testuser",
#                                 "email": "test@example.com",
#                                 "password1": "tetspassword",
#                                 "password2": "testpassword"})
#         self.assertFalse(form.is_valid())
#         self.assertEqual(
#             form.errors["password2"], [u"Passwords do not match. Please enter matching passwords."])
            
    
# class TestUserUpdateForm(TestCase):
#     def test_username_update(self):
#         form = UserUpdateForm({"email": "newtestuser"})
#         form.save()
#         self.assertTrue(form.is_valid())
        
#     def test_email_update(self):
#         form = UserUpdateForm({"email": "newemail@example.com"})
#         form.save()
#         self.assertTrue(form.is_valid())
        
# class TestProfileUpdateForm(TestCase):
    
#     def test_profile_image_update(self):

# Views

class TestHomeView(TestCase):
    def test_index_view(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "home.html")

class TestLoginView(TestCase):
    def test_login_view(self):
        page = self.client.get("/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")


class TestLogoutView(TestCase):
    def test_logout_view(self):
        page = self.client.get("/logout/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse("login"))


class TestRegisterView(TestCase):
    def test_register_view(self):
        page = self.client.get("/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "register.html")


class TestProfileView(TestCase):
    def test_profile_view(self):
        page = self.client.get("/profile/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse("profile"))