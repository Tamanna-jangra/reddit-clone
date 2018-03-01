from django import forms
from .models import Posts,SubReddits,Subscriptions,Comments

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=['text','detail']