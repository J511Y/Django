import json
from django.views import View
from django.http import JsonResponse
from django.shortcuts import *
from .models import *
from .forms import *
from datetime import datetime
from django.contrib.auth import authenticate
from studyProject.util import *
from studyProject.common import *
from studyProject.decorate import *

# Create your views here.


class DailyDetail(View):
    @LoginAuth
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


# ajax 요청

class DailyLikeClick(View):
    def post(self, request):
        return ErrorMsg("올바르지 않은 접근입니다.", "main")

    @LoginAuth
    def get(self, request):
        data = request.GET
        login_id = request.session.get('login_id')
        if DailyLike.objects.filter(user_id=login_id, daily_id=data['daily_id']).exists():
            DailyLike\
                .objects\
                .get(
                    user_id=login_id, daily_id=data['daily_id']
                ).delete()
        else:
            DailyLike.objects.create(
                user_id=User.objects.get(id=login_id),
                daily_id=Daily.objects.get(id=data['daily_id']),
            )

        return HttpResponse(DailyLike.objects.filter(daily_id=data['daily_id']).count())


class DailyBookmarkClick(View):
    def post(self, request):
        return ErrorMsg("올바르지 않은 접근입니다.", "main")

    @LoginAuth
    def get(self, request):
        data = request.GET
        login_id = request.session.get('login_id')
        if Bookmark.objects.filter(user_id=login_id, daily_id=data['daily_id']).exists():
            Bookmark\
                .objects\
                .get(
                    user_id=login_id, daily_id=data['daily_id']
                ).delete()
        else:
            Bookmark.objects.create(
                user_id=User.objects.get(id=login_id),
                daily_id=Daily.objects.get(id=data['daily_id']),
            )

        return HttpResponse(Bookmark.objects.filter(daily_id=data['daily_id']).count())

class Profile(View):
    @LoginAuth
    def get(self,request):
        login_id = request.session.get('login_id', None)
        return render(request, 'user/profile.html',{'id': login_id})

class DailyLike(View):
    @LoginAuth
    def get(self, request):
        return render(request, 'daily/like.html')