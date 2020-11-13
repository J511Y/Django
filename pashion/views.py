from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from studyProject import settings
from studyProject.common import *
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


# 현재 위치 날씨 정보
def weather(request):
    data = request.GET
    print(data)
    param = {
        'lat': data.get('lat'),
        'lon': data.get('lon'),
        'appid': settings.WEATHER_KEY,
        'lang': 'kr',
    }
    weather_data = JsonAPIRequest('http://api.openweathermap.org/data/2.5/weather', param, 'GET')
    return JsonResponse({'data': weather_data}, status = 200)

def profile(request):
    return render(request, 'profile.html')


def daily_like(request):
    return render(request, 'like.html')
