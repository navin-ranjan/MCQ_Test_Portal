from django.urls import path
from django.contrib import admin
from Student import views


urlpatterns = [
    path('', views.student_login,name='studentlogin'),
    path('Studentsignup/', views.student_signup,name='studentsignup'),
    #path('Studentregister/', views.sturdentregister,name='studentregister'),
    path('StudentDashboard/', views.student_dash,name='studentdash'),
    path('StudentResult/', views.student_result,name='studentresult'),
    path('StudentProfile/', views.student_profile,name='studentprofile'),
    path('ExamInstrucion/<str:subject>', views.exam_instruction,name='examinstruction'),
    path('ExamTake/<str:subject>', views.exam_take,name='examtake'),
    path('ExamResult/', views.exam_result,name='examresult'),
    
    
]