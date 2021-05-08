from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.views import View
from django.http import HttpResponse

# Create your views here

def teacher_login(request):
    if request.POST:
        username=request.POST['username']
        upass=request.POST['upass']

        count =Teacher.objects.filter(username=username,password=upass).count()
        if count >0:
            return HttpResponse("login successfully!")
        else:
            messages.warning(request,'Username Or Password not correct ')
    return render(request,'Teacher/teacherlog.html')    
