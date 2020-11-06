from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from daily import views

app_name = "daily"

urlpatterns = [
    #path('', views.index, name='index'),
    path('<int:daily_id>/', DailyDetail.as_view(), name="detail"),
    path('upload/', DailyDetail.as_view(), name="upload"),
    path('userlike/', DailyLike.as_view(), name="like"),
    # path('like/', DailyLikeClick.as_view(), name="daily_like"),
    path('bookmark/', DailyBookmarkClick.as_view(), name="daily_bookmark"),
]