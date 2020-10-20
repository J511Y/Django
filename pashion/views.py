from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import User

# Create your views here.
def home(request):
    users = User.objects.all()
    return render(request, "home.html", {'users' : users})

def profile(request, id):
    user = get_object_or_404(User, pk = id)
    return render(request, 'profile.html', {'user' : user})