# 모든 app에서 공통적으로 사용하는 함수와 클래스를 모아놓은 곳
# 공통으로 사용되는 부분이므로 작성 및 수정을 조심스레 해야됨
import json
from django.views import View
from django.http import JsonResponse
from django.shortcuts import *
from datetime import datetime


# 에러 발생
def ErrorMsg(request, msg):
    return render(request, 'error.html', {'msg': msg})


# Ajax 요청 시 json 에러 발생
def ErrorMsgJson(request, msg):
    return JsonResponse({'message': msg}, status=400)
