from django.urls import path
from django.contrib import admin
from Student import views


urlpatterns = [
    path('', views.student_login,name='studentlogin'),
    path('Studentsignup/', views.student_signup,name='studentsignup'),
    #path('Studentregister/', views.sturdentregister,name='studentregister'),
    path('StudentDashboard/', views.sturdent_dash,name='studentdash'),
    path('StudentResult/', views.sturdent_result,name='studentresult'),
    path('StudentProfile/', views.sturdent_profile,name='studentprofile'),
    
    
]