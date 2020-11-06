import json
from django.views import View
from django.http import JsonResponse
from django.shortcuts import *
from .models import User
from .forms import *
from datetime import datetime
from django.contrib.auth import authenticate
from studyProject.util import *
from studyProject.common import *
from studyProject.decorate import *

# Create your views here.

crypt = SimpleEnDecrypt()

class Regist(View):
    def post(self, request):
        data = request.POST
        form = UserRegistForm(data)

        if User.objects.filter(id=data['id']).exists():
            return render(request, 'user/regist.html', {'form': form, 'id': 'is-invalid'})

        if data['password'] != data['password_chk']:
            return render(request, 'user/regist.html', {'form': form, 'password': 'is-invalid'})

        if form.is_valid():
            # 저장 전 비밀번호 암호화 작업
            post = form.save(commit=False)
            post.password = crypt.encrypt(data['password'])
            post.password_chk = crypt.encrypt(data['password_chk'])
            post.save()

            form = UserLoginForm()
            return render(request, 'user/login.html', {'form': form, 'regist': True})
        else:
            return render(request, 'user/regist.html', {'form': form})

    def get(self, request):
        form = UserRegistForm()
        return render(request, 'user/regist.html', {'form': form})


class Login(View):
    form = UserLoginForm()

    def post(self, request):
        data = request.POST
        self.form = UserLoginForm(data)
        
        password = crypt.decrypt(User.objects.filter(id=data['id'])[0].password)
        
        if User.objects.filter(id=data['id']).exists() and password == data['password']:
            request.session['login_id'] = data['id']
            return redirect("/")
        else:
            return render(request, 'user/login.html', {'form': self.form})

    def get(self, request):
        login_id = request.session.get('login_id', None)
        if login_id is not None and User.objects.filter(id=login_id).exists():
            return render(request, 'main.html')
        return render(request, 'user/login.html', {'form': self.form})


# login required
class Logout(View):
    @LoginAuth
    def get(self, request):
        request.session.pop('login_id')
        return redirect("/")

class Profile(View):
    @LoginAuth
    def get(self,request):
        login_id = request.session.get('login_id', None)
        user = User.objects.get(id=login_id)
        return render(request, 'user/profile.html',{'user' : user})

class Profile_update(View):
    @LoginAuth
    def get(self,request):
        login_id = request.session.get('login_id', None)        
        user = User.objects.get(id=login_id)
        return render(request, 'user/profile_update.html',{'user' : user})
