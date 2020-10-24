from django.db import models
from user.models import User

# 데일리 게시글 모델


class Daily(models.Model):
    # 게시자 ID
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # 게시글 이미지
    daily_image = models.ImageField(
        null=True, upload_to='images/', blank=True)

    # 게시글 내용
    content = models.TextField()

    # 좋아요
    like = models.IntegerField(default=0)

    # 읽은 수
    read = models.IntegerField(default=0)

    # 게시일
    create_day = models.DateTimeField(auto_now_add=True)

    # 수정일
    update_day = models.DateTimeField(auto_now=True)

    # 스타일 태그
    style_tag = models.TextField(null=True, blank=True)

    def __str__(self):
        return ''
