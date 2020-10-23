from django.shortcuts import render, get_object_or_404

# Create your views here.


def main(request):
    return render(request, "main.html")


def profile(request):
    return render(request, 'profile.html')
