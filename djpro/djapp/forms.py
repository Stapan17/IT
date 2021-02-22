from django import forms
from .models import userInfo
from django.contrib.auth.models import User


class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['email', 'username', 'password']


class userInfoForm(forms.ModelForm):
    class Meta():
        model = userInfo
        fields = ['name', 'phone', 'profile_pic']
