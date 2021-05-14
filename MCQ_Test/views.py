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

def admin_delete_student(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        pi.delete()
    st=Student.objects.all()
    return render(request,'MCQ_Test/adminstudent.html',{'stu':st})

def admin_edit_student(request,id):
    stu=Student.objects.get(pk=id)
    if request.method=='POST':
        username=request.POST['username']          
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        umobile=request.POST['umobile']
        upass=request.POST['upass']
        stu.username=username
        stu.name=uname
        stu.email=uemail
        stu.mobile=umobile
        stu.password=upass
        stu.save()
        return redirect('adminstudent')
    return render(request,'MCQ_Test/adminstudentedit.html',{'stu':stu})


def admin_teacher(request):
    te=Teacher.objects.all()
    return render(request,'MCQ_Test/adminteacher.html',{'tech':te})

def admin_edit_teacher(request,id):
    stu=Teacher.objects.get(pk=id)
    if request.method=='POST':
        username=request.POST['username']          
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        umobile=request.POST['umobile']
        upass=request.POST['upass']
        stu.username=username
        stu.name=uname
        stu.email=uemail
        stu.mobile=umobile
        stu.password=upass
        stu.save()
        return redirect('adminteacher')
    return render(request,'MCQ_Test/adminteacheredit.html',{'stu':stu})

def admin_delete_teacher(request,id):
    if request.method=='POST':
        pi=Teacher.objects.get(pk=id)
        pi.delete()
    te=Teacher.objects.all()
    return render(request,'MCQ_Test/adminteacher.html',{'tech':te})

def admin_add_teacher(request):
    se=Subject.objects.all()
    if request.POST:
        username=request.POST['username']          
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        usubject=request.POST['usubject']
        umobile=request.POST['umobile']
        upass=request.POST['upass']
        subject=Subject.objects.get(id=usubject)
        if Teacher.objects.filter(username=username).exists():
            messages.warning(request,'Username is already exists')
        else:    
            Teacher.objects.create(username=username,name=uname,email=uemail,subject=subject,mobile=umobile,password=upass)
            messages.success(request,'New Teacher has been Added Successfully')
        
    return render(request,'MCQ_Test/adminteacheradd.html',{'sub':se})

def admin_subject(request):
    sub=Subject.objects.all()
    return render(request,'MCQ_Test/adminsubject.html',{'sub':sub})

def admin_add_subject(request):
    if request.POST:
        sub=request.POST['subject'] 
        if Subject.objects.filter(subject=sub).exists():
            messages.warning(request,'Subject is already exists')
        else:
            obj=Subject(subject=sub)
            obj.save()
            messages.success(request,'Subject add successful')

    return render(request,'MCQ_Test/adminsubjectadd.html')

def admin_contact(request):
    con=Contacts.objects.all()
    return render(request,'MCQ_Test/admincontact.html',{'cont':con})

def admin_delete_contact(request,id):
    if request.method=='POST':
        pi=Contacts.objects.get(pk=id)
        pi.delete()
    con=Contacts.objects.all()
    return render(request,'MCQ_Test/admincontact.html',{'cont':con})
