from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from Student.models import *
from Teacher.models import *

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
    if request.POST:
        username=request.POST['username']
        upass=request.POST['upass']
        if (username =="admin" and upass=="admin12345"):
            return redirect('admindash')
        else:
            messages.warning(request,'Username Or Password not correct ')
    return render(request,'MCQ_Test/adminweb.html')


def admin_dash(request):
    return render(request,'MCQ_Test/admindash.html')

def admin_student(request):
    st=Student.objects.all()
    return render(request,'MCQ_Test/adminstudent.html',{'stu':st})

def admin_teacher(request):
    te=Teacher.objects.all()
    return render(request,'MCQ_Test/adminteacher.html',{'tech':te})

def admin_subject(request):
    return render(request,'MCQ_Test/adminsubject.html')

def admin_contact(request):
    con=Contacts.objects.all()
    return render(request,'MCQ_Test/admincontact.html',{'cont':con})
