from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from daily import views

app_name = "daily"

urlpatterns = [
    #path('', views.index, name='index'),
    path('<int:daily_id>/', DailyDetail.as_view(), name="detail"),
    path('upload/', DailyDetail.as_view(), name="upload"),
    path('like/', UserToDailyAction.as_view(), name="daily_like_action"),
    path('bookmark/', UserToDailyAction.as_view(), name="daily_bookmark_action"),
]
