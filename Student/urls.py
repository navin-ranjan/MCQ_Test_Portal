from django.urls import path
from django.contrib import admin
from Student import views


urlpatterns = [
    path('', views.student_login,name='studentlogin'),
    path('Studentsignup/', views.student_signup,name='studentsignup'),
    path('Studentregister/', views.sturdentregister,name='studentregister'),
    
    
]