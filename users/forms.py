from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class ProfileUpdateform(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']