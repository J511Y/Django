from django import forms
from .models import User


class UserRegistForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id', 'password', 'password_chk',
                  'name', 'nickname', 'phone']


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id', 'password']