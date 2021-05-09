from django.urls import path
from . import views
from MCQ_Test import views


urlpatterns = [
    path('', views.home_page,name="Exampath"),
    path('ContactUs/', views.contact_us,name="Contactpath"),
    path('AdminWeb/', views.admin_web,name="Adminpath"),
    path('Admindashboard/', views.admin_dash,name="admindash"),
    path('Adminstudent/', views.admin_student,name="adminstudent"),
    path('Adminteacher/', views.admin_teacher,name="adminteacher"),
    path('Adminsubject/', views.admin_subject,name="adminsubject"),
    path('Admindcontact/', views.admin_contact,name="admincontact"),


]
