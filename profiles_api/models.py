from lib2to3.pytree import Base
from django.db import models
#Importing models needed for a user class
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new User Profile"""
        if(not email):
            raise ValueError("Users must have an email address")
        
        #converting the second half of the email to lowercase
        email = self.normalize_email(email)

        user = self.model(email=email, name=name)

        #converting the password into a hash
        user.set_password(password)
        
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff=True
        user.save(using=self._db)

        return user


#Our new user class
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model fro users in the system"""
    #creating fields for the user class
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()
    
    #overriding the default username field to email
    USERNAME_FIELD = 'email'

    #Setting the required fields  to a list of required fields
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    
    def __str__(self):
        """Return string representation of user"""
        return self.email