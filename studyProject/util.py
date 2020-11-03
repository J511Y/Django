import json
from django.views import View
from django.http import JsonResponse
from datetime import datetime
from django.shortcuts import *

# 말 그대로 유틸 ㅇㅅㅇ
# 주로 함수들을 모아놓으며 귀찮은 기능들을 모듈화 해놓음
# 데코레이터들이 주로 모아질듯?





############ 데코레이터 ########
# 로그인 여부 확인
def LoginAuth(func):

    def wrapper(func_self, request, *args, **kwargs):
        login_id = request.session.get('login_id', None)
        if(login_id == None):
            return render(request, 'user/login.html')
        return func(func_self, request)

    return wrapper


# 관리자 여부 확인
def AdminAuth(func):
    def wrapper(func_self, request, *args, **kwargs):
        isAdmin = request.session.get('isAdmin', None)
        if(isAdmin == None):
            return ridirect("/")
        return func(func_self, request)

    return wrapper
