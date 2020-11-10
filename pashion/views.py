from django.shortcuts import render, get_object_or_404
from daily.models import *
from daily.forms import *

from user.models import *
from user.forms import *

# Create your views here.


def main(request):
    data = {}
    # 데일리 게시글
    daily_query = '''
        SELECT
            A.*
            , (SELECT COUNT(*) FROM daily_dailylike B WHERE A.id = B.daily_id) AS like
            , (SELECT COUNT(*) FROM daily_bookmark B WHERE A.id = B.daily_id) AS bookmark
            , (SELECT COUNT(*) FROM daily_dailyreply B WHERE A.id = B.daily_id) AS reply
        FROM 
            daily_daily A
        ORDER BY A.create_day DESC
    '''
    data["Daily"] = Daily.objects.raw(daily_query)[:6]
    data["DailyForm"] = DailyForm()

    return render(request, "main.html", data)


def profile(request):
    return render(request, 'profile.html')


def daily_like(request):
    return render(request, 'like.html')
