from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# 회원 모델

class User(models.Model):
    # ID
    
    id = models.CharField(primary_key=True, max_length=15,null=False)

    # PW
    password = models.CharField(max_length=256, null=True)

    # PW check
    password_chk = models.CharField(max_length=256, null=True)

    # 변경 비밀번호
    newpassword = models.CharField(max_length=256)

    # 가입일
    create_day = models.DateTimeField(auto_now_add=True)

    # 수정일
    update_day = models.DateTimeField(auto_now=True)

    # 핸드폰번호
    phone = models.CharField(max_length=15, null=True, blank=False)

    # 이름
    name = models.CharField(null=False, blank=False, max_length=10)

    # 나이
    birthday = models.CharField(
        null=False, blank=False, max_length=15, default='0000-00-00')

    # 이메일
    email = models.EmailField(null=True, blank=True)

    # 프로필 이미지
    profile_image = models.ImageField(
        null=True, upload_to='images/', blank=True)

    # 닉네임
    nickname = models.CharField(max_length=10, null=False, blank=False)

    # 프로필 설명
    description = models.TextField(null=True, blank=True)

    # 즐겨입는 스타일
    like_style = models.TextField(null=True, blank=True)

    # 유저 타입 (1:일반유저, 99:관리자)
    user_type = models.IntegerField(default=1)

    def __str__(self):
        return self.name + '(' + self.nickname + ')'

<<<<<<< HEAD
=======
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # User모델과 Profile을 1:1로 연결 ==> OneToOneField
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
    profile_image = models.ImageField(blank=True)
>>>>>>> c3746f84a0ef2ce485e8eaf5bdef8643aff5a323

