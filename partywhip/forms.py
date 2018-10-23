from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    # username = forms.CharField(label="Username")
    # password1 = forms.CharField()
    # password2 = forms.CharField()

    class Meta:
        model = User
        help_text = {
            'username': None,
            'password': None,
            'password2': None,
        }

        widgets = {

            'username': forms.TextInput(attrs={'placeholder': 'Enter a username'}),
            'password': forms.TextInput(attrs={'placeholder': 'Enter a password'}),
            'password2': forms.TextInput(attrs={'placeholder': 'Confirm your password'})
        }

        exclude = ('groups', 'last_login', 'password', 'is_superuser', 'user_permissions', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined')
