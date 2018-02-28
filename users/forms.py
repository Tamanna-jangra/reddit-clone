# Django comes with two forms for the default User model that we’ll need to customize:
# UserCreationForm and UserChangeForm.
from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=UserCreationForm.Meta.fields

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=UserChangeForm.Meta.fields