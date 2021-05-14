from django.shortcuts import render,redirect
from . models import *
from MCQ_Test.models import *
from django.contrib import messages
from django.views import View

# Create your views here

def teacher_login(request):
    if request.POST:
        username=request.POST['username']
        upass=request.POST['upass']

        count =Teacher.objects.filter(username=username,password=upass).count()
        if count >0:
            return redirect('teacherdash')
        else:
            messages.warning(request,'Username Or Password not correct ')
    return render(request,'Teacher/teacherlog.html')    

def teacher_dash(request):
  return render(request,'Teacher/teacherdash.html') 

def teacher_question(request):
    ques=Question.objects.all()
    return render(request,'Teacher/teacherquestion.html',{'ques':ques})    

def teacher_add_question(request):
    return render(request,'Teacher/teacheraddquestion.html') 

def teacher_profile(request):
  return render(request,'Teacher/teacherprofile.html')         