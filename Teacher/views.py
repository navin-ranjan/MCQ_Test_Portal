from django.shortcuts import render,redirect
from . models import *
from MCQ_Test.models import *
from django.contrib import messages
from django.views import View

# Create your views here


def teacher_login(request):
    global tuser
    if request.POST:
        username=request.POST['username']
        upass=request.POST['upass']

        count =Teacher.objects.filter(username=username,password=upass).count()
        if count >0:
            tuser=username
            return redirect('teacherdash')
        else:
            messages.warning(request,'Username Or Password not correct ')
    return render(request,'Teacher/teacherlog.html')    

def teacher_dash(request): 
    global se
    sub=Teacher.objects.filter(username=tuser)
    for i in sub:
        se=i.subject
    ques=Question.objects.filter(subject=se)
    return render(request,'Teacher/teacherdash.html',{'ques':ques,'sub':se}) 
    
def teacher_add_question(request):
    if request.POST:
        ques=request.POST['aquestion'] 
        mark=request.POST['amark']         
        optn1=request.POST['aoption1']
        optn2=request.POST['aoption2']
        optn3=request.POST['aoption3']
        optn4=request.POST['aoption4']
        ans=request.POST['aanswer']           
        Question.objects.create(question=ques,marks=mark,subject=se,option1=optn1,option2=optn2,option3=optn3,option4=optn4,answer=ans)
        messages.success(request,'New Teacher has been Added Successfully')
    return render(request,'Teacher/teacheraddquestion.html') 

def teacher_delete_question(request,id):
    if request.method=='POST':
        pi=Question.objects.get(pk=id)
        pi.delete()
    ques=Question.objects.filter(subject=se)
    return render(request,'Teacher/teacherdash.html',{'ques':ques,'sub':se})

def teacher_edit_question(request,id):
    ques=Question.objects.get(pk=id)
    if request.method=='POST':
        qu=request.POST['aquestion']          
        mark=request.POST['amark']
        optn1=request.POST['aoption1']
        optn2=request.POST['aoption2']
        optn3=request.POST['aoption3']
        optn4=request.POST['aoption4']
        ans=request.POST['aanswer']
        ques.question=qu
        ques.marks=mark
        ques.option1=optn1
        ques.option2=optn2
        ques.option3=optn3
        ques.option4=optn4
        ques.answer=ans
        ques.save()
        return redirect('teacherdash')
    return render(request,'Teacher/teachereditquestion.html',{'ques':ques})  

def teacher_profile(request):
    te=Teacher.objects.get(username=tuser)
    return render(request,'Teacher/teacherprofile.html',{'pr':te})         