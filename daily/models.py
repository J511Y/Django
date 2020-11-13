from django.db import models
from user.models import User

# 데일리 게시글 모델


class Daily(models.Model):
    # 게시자 ID
    user_id = models.ForeignKey(
        User, db_column='user_id', on_delete=models.CASCADE)

    # 게시글 이미지
    daily_image = models.ImageField(
        null=True, upload_to='images/', blank=True)

    # 게시글 내용
    content = models.TextField()

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

# 북마크 / 좋아요 남긴 게시글 ( 추후 통합 필요 )
class Bookmark(models.Model):
    # 유저 ID
    user_id = models.ForeignKey(
        User, db_column='user_id', on_delete=models.CASCADE)

    # 게시글 번호
    daily_id = models.ForeignKey(
        Daily, db_column='daily_id', on_delete=models.CASCADE)


class DailyLike(models.Model):
    # 유저 ID
    user_id = models.ForeignKey(
        User, db_column='user_id', on_delete=models.CASCADE)

    # 게시글 번호
    daily_id = models.ForeignKey(
        Daily, db_column='daily_id', on_delete=models.CASCADE)

# 데일리 게시글 댓글 모델


class DailyReply(models.Model):
    # 유저 ID
    user_id = models.ForeignKey(
        User, db_column='user_id', on_delete=models.CASCADE)

    # 게시글 번호
    daily_id = models.ForeignKey(
        Daily, db_column='daily_id', on_delete=models.CASCADE)

    # 내용
    content = models.TextField(null=False, blank=False)

    # 작성일
    create_day = models.DateTimeField(auto_now_add=True)

    # 수정일
    update_day = models.DateTimeField(auto_now=True)

    # 원댓글 번호
    ref = models.IntegerField()

    # 대댓글 번호
    ref_num = models.IntegerField(default=1)
