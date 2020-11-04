from studyProject.common import *


############ 데코레이터 ########
# 로그인 여부 확인
def LoginAuth(func):

    def wrapper(func_self, request, *args, **kwargs):
        login_id = request.session.get('login_id', None)
        if(login_id == None):
            return ErrorMsg(request, "로그인이 필요합니다")
        return func(func_self, request)

    return wrapper


# 관리자 여부 확인
def AdminAuth(func):
    def wrapper(func_self, request, *args, **kwargs):
        isAdmin = request.session.get('isAdmin', None)
        if(isAdmin == None):
            return ErrorMsg(request, "관리자만 접근 가능합니다.")
        return func(func_self, request)

    return wrapper
