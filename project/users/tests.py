from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import reverse
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm



# Forms

class TestUserRegistrationForm(TestCase):
    def test_registration_valid(self):
            form = UserRegisterForm({'username':"testuser",
                                         "email": "test@example.com",
                                         "password1": "test_password",
                                         "password2": "test_password",
                                         })
            self.assertTrue(form.is_valid())
            
    def test_passwords_do_not_match(self):
        form = UserRegisterForm({"username": "TestUser",
                                "email": "Test@Email.com",
                                "password1": "tetspassword",
                                "password2": "testpassword"})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["password2"], [u"Passwords do not match. Please enter matching passwords."])
            
    
# class TestUserUpdateForm(TestCase):

# class TestProfileUpdateForm(TestCase):

# Views

# profile

# login

# logout

# register