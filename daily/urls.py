from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = "daily"

urlpatterns = [
    #path('', views.index, name='index'),
    path('<int:daily_id>/', DailyDetail.as_view(), name="detail"),
    path('upload/', DailyDetail.as_view(), name="upload"),
]
