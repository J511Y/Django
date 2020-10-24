import json
from django.views import View
from django.http import JsonResponse
from django.shortcuts import *
from .models import User
from .forms import *
from datetime import datetime
from django.contrib.auth import authenticate

# Create your views here.


class DailyDetail(View):
    def post(self, request):
        data = request.POST
        form = DailyForm(data)

        if User.objects.filter(id=data['id']).exists():
            return render(request, 'daily/regist.html', {'form': form, 'id': 'is-invalid'})

        if data['password'] != data['password_chk']:
            return render(request, 'daily/regist.html', {'form': form, 'password': 'is-invalid'})

        if form.is_valid():
            form.save()
            form = DailyForm()
            return render(request, 'daily/login.html', {'form': form, 'regist': True})
        else:
            return render(request, 'daily/regist.html', {'form': form})

    def get(self, request):
        data = request.GET

        form = DailyForm(data)
        return render(request, 'daily/upload.html', {'form': form})
