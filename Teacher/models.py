from django.db import models
from MCQ_Test.models import *
# Create your models here.

class Teacher(models.Model):
    username=models.CharField(max_length=20)
    name=models.CharField(max_length=50)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    email=models.EmailField(max_length=100)
    mobile= models.CharField(max_length=11)
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.username