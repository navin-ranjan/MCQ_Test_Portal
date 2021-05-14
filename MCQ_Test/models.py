from django.db import models
from Student.models import Student
# Create your models here.
class Subject(models.Model):
   subject = models.CharField(max_length=50)
   def __str__(self):
       return self.subject
   

class Question(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

class Contacts(models.Model):
    name= models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone_no= models.CharField(max_length=13)
    massege= models.CharField(max_length=200)
    