from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import CustomUser
# Register your models here.
# The final step is to update our admin.py file. The default User model is tightly coupled
# to the Django admin. After all we can view and modify users within the admin so it
# makes sense we need to tell the admin about our new CustomUser model

class CustomUserAdmin(UserAdmin):
    model=CustomUser
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm

admin.site.register(CustomUser,CustomUserAdmin)