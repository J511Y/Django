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
    def get(self, request, daily_id):
        data = request.GET
        if(Daily.objects.filter(id=daily_id).exists() == False):
            return ErrorMsg("존재하지 않는 게시글입니다.", "main.html")

        daily = Daily.objects.get(id=daily_id)
        reply = DailyReply.objects.filter(
            daily_id=daily_id).order_by('ref', 'ref_num')
        return render(request, 'daily/post.html', {'daily': daily, 'reply': reply})


class DailyUpload(View):
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


class UserToDailyAction(View):
    def post(self, request):
        return ErrorMsg("올바르지 않은 접근입니다.", "main")

    @LoginAuth
    def get(self, request):
        data = request.GET
        login_id = request.session.get('login_id')

        if(data['action'] == 'like'):
            Object = DailyLike
        else:
            Object = Bookmark

        if Object.objects.filter(user_id=login_id, daily_id=data['daily_id']).exists():
            Object\
                .objects\
                .get(
                    user_id=login_id, daily_id=data['daily_id']
                ).delete()
        else:
            Object.objects.create(
                user_id=User.objects.get(id=login_id),
                daily_id=Daily.objects.get(id=data['daily_id']),
            )

        count = DailyLike.objects.filter(daily_id=data['daily_id']).count()
        return HttpResponse("|||SUCCESS|||" + str(count))


class UserToDailyLike(View):
    @LoginAuth
    def get(self, request):
        return render(request, 'daily/like.html')


class DailyDetailDelete(View):
    def get(self, request, id):
        daily = Daily.objects.get(id=id)
        daily.delete()
        return redirect("/")


class ReplyCreate(View):
    @LoginAuth
    def post(self, request, id):
        data = request.POST
        if 'ref' in data and data['ref']:
            ref_num = DailyReply.objects.filter(
                daily_id=id, ref=data['ref']).count() + 1
            ref = data['ref']
        else:
            ref_num = 1
            ref = DailyReply.objects.filter(daily_id=id).count() + 1

        reply = DailyReply(
            daily_id=Daily.objects.get(id=id),
            content=data['content'],
            user_id=User.objects.get(id=request.session.get('login_id')),
            ref=ref,
            ref_num=ref_num
        )

        reply.save()
        return redirect("/daily/" + str(id))


class ReplyDelete(View):
    def get(self, request, id):
        reply = DailyReply.objects.get(pk=id)
        reply.delete()
        return redirect("/daily/" + str(reply.daily_id.id))
