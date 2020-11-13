from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from daily import views

app_name = "daily"

urlpatterns = [
    #path('', views.index, name='index'),
    path('<int:daily_id>/', DailyDetail.as_view(), name="detail"),
    path('upload/', DailyUpload.as_view(), name="upload"),
    path('action/', UserToDailyAction.as_view(), name="action"),
    path('like/', UserToDailyLike.as_view(), name="like"),
    path('delete/<int:id>/', DailyDetailDelete.as_view(), name="delete"),
    path('replydelete/<int:id>/', ReplyDelete.as_view(), name="replydelete"),
    path('daily/<int:id>/', DailyDetail.as_view(), name="daily"),
    path('reply/<int:id>/', ReplyCreate.as_view(), name="reply"),

]