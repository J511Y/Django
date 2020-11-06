from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = "user"

urlpatterns = [
    path('regist/', Regist.as_view(), name="regist"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
<<<<<<< HEAD
    path('profile/', Profile.as_view(), name="profile"),
    path('profile_update/', Profile_update.as_view(), name="profile_update")

=======
    path('profile/', Profile.as_view(), name="profile")
>>>>>>> c3746f84a0ef2ce485e8eaf5bdef8643aff5a323
]
