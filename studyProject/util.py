import json
from django.views import View
from django.http import JsonResponse
from datetime import datetime
from django.shortcuts import *

from studyProject.common import *
from studyProject.decorate import *

from user.models import *

# 말 그대로 유틸 ㅇㅅㅇ
# 주로 함수들을 모아놓으며 귀찮은 기능들을 모듈화 해놓음

# 로그인 유저 반환
@LoginAuth
def GetLoginUser(self, request):
    return User.objects.get(id=request.session.get('login_id'))[0]