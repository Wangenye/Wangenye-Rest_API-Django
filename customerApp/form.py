from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'phone', 'password1', 'password2', )