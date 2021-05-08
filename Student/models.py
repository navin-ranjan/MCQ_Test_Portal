from django.db import models
# Create your models here.
class Student(models.Model):
    username=models.CharField(max_length=20, unique=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    mobile= models.CharField(max_length=11)
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.username


   
   