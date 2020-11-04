from django import forms
from user.models import User
from .models import *


class DailyForm(forms.ModelForm):
    class Meta:
        model = Daily
        fields = ['content', 'daily_image', 'style_tag', 'user_id']


class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['daily_id', 'user_id']


class DailyLikeForm(forms.ModelForm):
    class Meta:
        model = DailyLike
        fields = ['daily_id', 'user_id']
