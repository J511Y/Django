from django import forms
from django.contrib.auth.forms import UserChangeForm
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

class UserEditForm(UserChangeForm):
    password = None        
    phone = forms.CharField(label='연락처', widget=forms.TextInput(
        attrs={'maxlength':'11',}), 
    )        
    name = forms.CharField(label='이름', widget=forms.TextInput(
        attrs={'maxlength':'8',}), 
    )        
    nickname = forms.CharField(label='닉네임', widget=forms.TextInput(
        attrs={'maxlength':'10',}), 
    )
    description = forms.CharField(label='자기소개', widget=forms.Textarea(
        attrs={'maxlength':'100',}), 
    )
    class Meta:
        model = User
        fields = ['phone', 'name', 'nickname', 'description']