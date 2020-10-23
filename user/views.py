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

        if User.objects.filter(id=data['id']).exists():
            return JsonResponse({'message': '이미 존재하는 아이디 입니다.'}, status=400)

        form = UserRegistForm(data)

        if form.is_valid():
            form.save()
            form = UserLoginForm()
            return render(request, 'user/login.html', {'form': form})
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
        login_id = request.session['login_id']
        if login_id is not None and User.objects.filter(id=login_id).exists():
            return render(request, 'main.html')
        return render(request, 'user/login.html', {'form': self.form})


class Logout(View):
    def post(self, request):
        request.session['login_id'] = None
        return render(request, 'main.html')

    def get(self, request):
        request.session['login_id'] = None
        return render(request, 'main.html')
