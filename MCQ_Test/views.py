from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.views import View
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render(request,'MCQ_Test/home.html')

def contact_us(request):
    if request.POST:          
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        umobile=request.POST['umobile']
        upass=request.POST['msg']
        obj=Contacts(name=uname,email=uemail,phone_no=umobile,massege=upass)
        obj.save()
        messages.success(request,'Massege send Successfully')

    return render(request,'MCQ_Test/contactus.html')

def admin_web(request):
    return render(request,'MCQ_Test/adminweb.html')