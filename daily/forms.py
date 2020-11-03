from django import forms
from user.models import User
from .models import *


class DailyForm(forms.ModelForm):
    class Meta:
        model = Daily
        fields = ['content', 'daily_image', 'style_tag', 'user_id']
