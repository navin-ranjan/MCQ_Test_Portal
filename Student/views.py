from django.shortcuts import render,redirect
from . models import *
#from .forms import StudentRegistration
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
# Create your views here.

def student_login(request):
    if request.POST:
        username=request.POST['username']
        upass=request.POST['upass']

        count = Student.objects.filter(username=username,password=upass).count()
        if count >0:
            return HttpResponse("login successfully!")
        else:
            messages.warning(request,'Username Or Password not correct ')

    return render(request,'Student/studentlog.html')

def student_signup(request):
    return render(request,'Student/studentsignup.html')

def sturdentregister(request):
    if request.POST:
        username=request.POST['username']          
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        umobile=request.POST['umobile']
        upass=request.POST['upass']
        if Student.objects.filter(username=username).exists():
            messages.warning(request,'Username is already exists')
        else :
            obj=Student(username=username,name=uname,email=uemail,mobile=umobile,password=upass)
            obj.save()
            messages.success(request,'User has been created Successfully')
    return redirect('studentsignup')
        
