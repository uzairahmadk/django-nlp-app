from django.db import models
from django.contrib.auth.base_user import BaseUserManager
import datetime
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Create your models here.
from django.contrib.auth.models import User
class Topics(models.Model):
    name = models.CharField(max_length=100)    
    def __str__(self):
        return self.name

class Supervision(models.Model):
    supervisor = models.CharField(max_length=100) 
    def __str__(self):
        return self.supervisor
class Blog(models.Model):
    hosts =  models.ForeignKey(User, on_delete=models.SET_NULL ,null=True)
    topics = models.ForeignKey(Topics, on_delete=models.SET_NULL ,null=True) #CAscade is waja se for eg agar Room del hogya to ye b hojaye
    name = models.CharField(max_length=255)
    description  = models.TextField(null=True,blank=True,max_length=1000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Machine (models.Model):   
     hosts =  models.ForeignKey(User, on_delete=models.SET_NULL ,null=True)
     mach = models.FileField(null=True)
     expiry = models.DateTimeField(auto_now=False)
     supe = models.ForeignKey(Supervision,on_delete=models.SET_NULL,null=True)
     topics = models.ForeignKey(Topics, on_delete=models.SET_NULL ,null=True) #CAscade is waja se for eg agar Room del hogya to ye b hojaye
     name = models.CharField(max_length=255)
     description  = models.TextField(null=True,blank=True,max_length=1000)
     updated = models.DateTimeField(auto_now=True)
     created = models.DateTimeField(auto_now=True)
     def __str__(self):
      return self.name
class Year(models.Model):
    year = models.DateField(max_length=100 ,null=True)
    def __str__(self):
      return self.year
    
class Department(models.Model):
    dept = models.CharField(max_length=50,null=True)
    def __str__(self):
      return self.dept
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ) #CAscade is waja se for eg agar Room del hogya to ye b hojaye
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE )
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.body[0:50]
class Technology(models.Model):
    tech = models.CharField(max_length=50 ,null=True)
    def __str__(self):
      return self.tech
  
class Project (models.Model):  
     name = models.CharField(max_length=255) 
     hosts =  models.ForeignKey(User, on_delete=models.SET_NULL ,null=True)
     supervisor = models.ForeignKey(Supervision,on_delete=models.SET_NULL,null=True)
    #  topics = models.ForeignKey(Topics, on_delete=models.SET_NULL ,null=True) #CAscade is waja se for eg agar Room del hogya to ye b hojaye
     technology = models.ForeignKey(Technology, on_delete=models.SET_NULL ,null=True)
     created = models.DateField(auto_now=False)
     description  = models.TextField(null=True,blank=True,max_length=1000)
     def __str__(self):
        return self.name

class Announcement (models.Model):  
     name = models.CharField(max_length=255) 
     hosts =  models.ForeignKey(User, on_delete=models.SET_NULL ,null=True)
     supervisor = models.ForeignKey(Supervision,on_delete=models.SET_NULL,null=True)
    #  topics = models.ForeignKey(Topics, on_delete=models.SET_NULL ,null=True) #CAscade is waja se for eg agar Room del hogya to ye b hojaye
     technology = models.ForeignKey(Technology, on_delete=models.SET_NULL ,null=True)
     created = models.DateField(auto_now=False)
     description  = models.TextField(null=True,blank=True,max_length=1000)
     def __str__(self):
        return self.name
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username,
            password=password,
        )

        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
       
class User(AbstractBaseUser):
    username = models.CharField(
        unique=True,
        max_length=50,
    )
    bio = models.TextField()

    is_active = models.BooleanField(default=True,
                                    verbose_name="Active",
                                    help_text="lorem")
    is_admin = models.BooleanField(default=False,
                                   verbose_name="Staff status",
                                   help_text="lorem")
    is_superuser = models.BooleanField(default=False,
                                       verbose_name="Superuser status",
                                       help_text="lorem")

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, db):
        return True
    @property
    def is_staff(self):
        return self.is_admin