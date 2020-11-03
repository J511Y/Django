from django.shortcuts import render, get_object_or_404
from daily.models import *
from daily.forms import *

from user.models import *
from user.forms import *

# Create your views here.


def main(request):
    data = {}
    data["Daily"] = Daily.objects.all()
    data["DailyForm"] = DailyForm()
    return render(request, "main.html", data)


def profile(request):
    return render(request, 'profile.html')
