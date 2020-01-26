from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import reverse
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import User
        
# Forms

## Register

class TestUserRegistrationForm(TestCase):
    def test_registration_valid(self):
            form = UserRegisterForm({'username':"testuser1",
                                         "email": "test@example.com",
                                         "password1": "test_password",
                                         "password2": "test_password",
                                         })
            self.assertTrue(form.is_valid())
            
    def test_passwords_do_not_match(self):
        form = UserRegisterForm({"username": "testuserA",
                                "email": "test@example.com",
                                "password1": "tetspassword",
                                "password2": "testpassword"})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["password2"], [u"The two password fields didn't match."])
            
    def test_email_missing(self):
        form = UserRegisterForm({"username": "testuserA",
                                "email": "",
                                "password1": "tetspassword",
                                "password2": "testpassword"})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["email"], [u"This field is required."])
            
    def test_username_missing(self):
        form = UserRegisterForm({"username": "",
                                "email": "test@example.com",
                                "password1": "tetspassword",
                                "password2": "testpassword"})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["username"], [u"This field is required."])

## Update

    def test_email_update(self):
        form = UserUpdateForm({"username": "testcaseuser", "email": "newemail@example.com"})
        form.save()
        self.assertTrue(form.is_valid())
        
    def test_email_bad_update(self):
        form = UserUpdateForm({"username": "testcaseuser", "email": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["email"], [u'This field is required.'])
            
    def test_email_bad_format_update(self):
        form = UserUpdateForm({"username": "testcaseuser", "email": "example"})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["email"], [u'Enter a valid email address.'])
    
## Username already exists

    def test_duplicate_username(self):
        self.user = User.objects.create_user(username='testuserC', password='testing321')
        form = UserRegisterForm({"username": "testuserC",
                                "email": "test@example.com",
                                "password1": "testpassword456",
                                "password2": "testpassword456"})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["username"], [u"A user with that username already exists."])
        

## Update Profile Image

    def test_profile_image_update(self):
        newImage = ProfileUpdateForm
        newImage.image = SimpleUploadedFile(
            "test_image.jpg", b"file_content", content_type="image/jpeg")
        self.client.post(reverse("profile"), {"newImage": newImage})
        self.assertIsNotNone(ProfileUpdateForm)

# Views

class TestLoginView(TestCase):
    def test_login_view(self):
        page = self.client.get("/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")


class TestLogoutView(TestCase):
    def test_logout_view(self):
        page = self.client.get("/logout/")
        self.assertEqual(page.status_code, 200)
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