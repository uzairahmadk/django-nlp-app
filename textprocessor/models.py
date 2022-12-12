from django.db import models

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