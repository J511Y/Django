import json
from django.views import View
from django.http import JsonResponse
from django.shortcuts import *
from .models import User
from .forms import *
from datetime import datetime
from django.contrib.auth import authenticate

# Create your views here.


class Regist(View):
    def post(self, request):
        data = request.POST
        form = UserRegistForm(data)

        if User.objects.filter(id=data['id']).exists():
            return render(request, 'user/regist.html', {'form': form, 'id': 'is-invalid'})

        if data['password'] != data['password_chk']:
            return render(request, 'user/regist.html', {'form': form, 'password': 'is-invalid'})

        if form.is_valid():
            form.save()
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

        if User.objects.filter(id=data['id'], password=data['password']).exists():
            request.session['login_id'] = data['id']
            return render(request, 'main.html')
        else:
            return render(request, 'user/login.html', {'form': self.form})

    def get(self, request):
        login_id = request.session.get('login_id', None)
        if login_id is not None and User.objects.filter(id=login_id).exists():
            return render(request, 'main.html')
        return render(request, 'user/login.html', {'form': self.form})


# login required
class Logout(View):
    def post(self, request):
        request.session['login_id'] = None
        return render(request, 'main.html')

    def get(self, request):
        request.session['login_id'] = None
        return render(request, 'main.html')
