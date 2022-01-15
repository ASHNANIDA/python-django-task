from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class student(models.Model):
        name=models.CharField(max_length=50,default="")
        email=models.CharField(max_length=20,default="")
        password=models.CharField(max_length=20,default="")
        rollno=models.IntegerField()
        college=models.CharField(max_length=30,default="")
        phoneno=models.IntegerField()
        
        def __str__(self):
            return self.name
class login(models.Model): 
      username=models.CharField(max_length=20)
      Password=models.CharField(max_length=20)
      def __str__(self):
            return self.username
class feedback(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    text=models.CharField(max_length=200)
    def __str__(self):
            return self.name