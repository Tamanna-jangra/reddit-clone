from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
# Create your models here.

# Under - the - hood in Django model managers are the actual interface for translating
# models into actual database queries. They handle the heavy lifting so we can just write
# simple Python in our model classes.
# We can create our own CustomUserManager and CustomUser by extending the model
# and manager used by Django for the default User. The existing model is called
# AbstractUser and its corresponding model manager is UserManager
class CustomUserManager(UserManager):
    pass
class CustomUser(AbstractUser):
    objects=CustomUserManager()    
