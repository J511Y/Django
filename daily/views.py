import json
from django.views import View
from django.http import JsonResponse
from django.shortcuts import *
from .models import User
from .forms import *
from datetime import datetime
from django.contrib.auth import authenticate
from studyProject import util
from studyProject import common

# Create your views here.


class DailyDetail(View):
    @util.LoginAuth
    def post(self, request):
        form = DailyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'daily/regist.html', {'form': form})

    def get(self, request):
        data = request.GET

        form = DailyForm(data)
        return render(request, 'daily/upload.html', {'form': form})
