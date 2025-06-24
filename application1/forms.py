
# from django import forms
# from django.core.exceptions import ValidationError
# import re
# from .models import User
# from django import forms

# # forms.py

# class SignupForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput, min_length=8)
#     email = forms.EmailField()
#     age = forms.IntegerField()
#     phone_number = forms.CharField(max_length=15)

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         # Check if email already exists in the database
#         if User.objects.filter(email=email).exists():
#             raise ValidationError('This email is already registered.')
#         return email

#     def clean_phone_number(self):
#         phone_number = self.cleaned_data.get('phone_number')
#         # Check if phone number already exists in the database
#         if User.objects.filter(phone_number=phone_number).exists():
#             raise ValidationError('This phone number is already registered.')
#         return phone_number

#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         # Password validation criteria
#         if not re.search(r'\d', password):  # Check for at least one number
#             raise ValidationError('Password must contain at least one number.')
#         if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # Check for at least one special character
#             raise ValidationError('Password must contain at least one special character.')
#         return password

#     def clean_age(self):
#         age = self.cleaned_data.get('age')
#         if age < 0:
#             raise ValidationError('Age must be a positive number.')
#         return age

# <------------------------------------------------>









































from django import forms
from django.core.exceptions import ValidationError
import re
from django.contrib.auth import get_user_model  # Use this to get the correct User model

User = get_user_model()  # Dynamically fetch the User model

class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    email = forms.EmailField()
    age = forms.IntegerField()
    phone_number = forms.CharField(max_length=15)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email is already registered.')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError('This phone number is already registered.')
        return phone_number

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:  # Ensure password exists before checking
            if not re.search(r'\d', password):  
                raise ValidationError('Password must contain at least one number.')
            if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  
                raise ValidationError('Password must contain at least one special character.')
        return password

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and age < 0:
            raise ValidationError('Age must be a positive number.')
        return age




