from django import forms
from .models import User


class UserRegistForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id', 'password', 'password_chk',
                  'name', 'nickname', 'phone', 'email']
        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'15자 이내로 입력 가능합니다.'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nickname': '닉네임',
            'email': '이메일',
            'password': '패스워드'
        }          


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id', 'password']
