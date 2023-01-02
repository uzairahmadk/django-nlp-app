from django.db import models# Create your models here.
from django.contrib.auth.models import User
class Topics(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

class Supervision(models.Model):
    supervisor = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.supervisor
    
class Department(models.Model):
    dept = models.CharField(max_length=50,null=True,unique=True)
    def __str__(self):
      return self.dept

class Technology(models.Model):
    tech = models.CharField(max_length=50 ,null=True,unique=True)
    def __str__(self):
      return self.tech
  
class Project (models.Model):  
    name = models.CharField(max_length=255,unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL ,null=True) #CAscade is waja se for eg agar Room del hogya to ye b hojaye
    supervisor = models.ForeignKey(Supervision,on_delete=models.SET_NULL,null=True)
    technology = models.ForeignKey(Technology, on_delete=models.SET_NULL ,null=True)
    hosts =  models.ForeignKey(User, on_delete=models.SET_NULL ,null=True)
    created = models.DateField(auto_now=True, null=True)
    description  = models.TextField(null=True,blank=True,max_length=1000)
    def __str__(self):
        return self.name

class Announcement (models.Model):  
     name = models.CharField(max_length=255) 
     hosts =  models.ForeignKey(User, on_delete=models.SET_NULL ,null=True)
     supervisor = models.ForeignKey(Supervision,on_delete=models.SET_NULL,null=True)
     technology = models.ForeignKey(Technology, on_delete=models.SET_NULL ,null=True)
     created = models.DateField(auto_now=False)
     description  = models.TextField(null=True,blank=True,max_length=1000)
     def __str__(self):
        return self.name