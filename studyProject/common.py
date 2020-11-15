# 모든 app에서 공통적으로 사용하는 함수와 클래스를 모아놓은 곳
# 공통으로 사용되는 부분이므로 작성 및 수정을 조심스레 해야됨
import json
import requests
from django.views import View
from django.http import JsonResponse
from django.shortcuts import *
from datetime import datetime
from cryptography.fernet import Fernet
from studyProject import settings
from daily.models import Daily
from user.models import User
import base64

# 암호화 클래스


class SimpleEnDecrypt:
    def __init__(self, key=None):
        if key is None:  # 키가 없다면
            key = settings.ENCRYPT_KEY  # 키를 생성한다
        self.key = key
        self.f = Fernet(self.key)

    def encrypt(self, data, is_out_string=True):
        if isinstance(data, bytes):
            ou = self.f.encrypt(data)  # 바이트형태이면 바로 암호화
        else:
            ou = self.f.encrypt(data.encode('utf-8'))  # 인코딩 후 암호화
        if is_out_string is True:
            return ou.decode('utf-8')  # 출력이 문자열이면 디코딩 후 반환
        else:
            return ou

    def decrypt(self, data, is_out_string=True):
        if isinstance(data, bytes):
            ou = self.f.decrypt(data)  # 바이트형태이면 바로 복호화
        else:
            ou = self.f.decrypt(data.encode('utf-8'))  # 인코딩 후 복호화
        if is_out_string is True:
            return ou.decode('utf-8')  # 출력이 문자열이면 디코딩 후 반환
        else:
            return ou

# 에러 발생


def ErrorMsg(request, msg, url):
    return render(request, 'error.html', {'msg': msg, 'url': url})


# Ajax 요청 시 json 에러 발생
def ErrorMsgJson(request, msg):
    return JsonResponse({'message': msg}, status=400)


# JSON 데이터로 API 요청
def JsonAPIRequest(URL, JSONData, method):
    if(method.lower() == 'get'):
        response = requests.get(URL, params=JSONData)
    else:
        response = requests.get(URL, data=json.dumps(JSONData))

    return response.json()
