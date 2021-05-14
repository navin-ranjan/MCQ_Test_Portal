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
    path('add_subject/', views.admin_add_subject,name="addsubject"),
    path('Admindcontact/', views.admin_contact,name="admincontact"),
    path('delete_student/<int:id>/',views.admin_delete_student,name="deletestudent"),
    path('delete_teacher/<int:id>/',views.admin_delete_teacher,name="deleteteacher"),
    path('delete_contact/<int:id>/',views.admin_delete_contact,name="deletecontact"),
    path('edit_student/<int:id>/',views.admin_edit_student,name="editstudent"),
    path('edit_teacher/<int:id>/',views.admin_edit_teacher,name="editteacher"),
    path('add_teacher/',views.admin_add_teacher,name="addteacher"),

]
