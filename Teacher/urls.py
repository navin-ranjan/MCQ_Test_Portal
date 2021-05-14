from django.urls import path
from . import views


urlpatterns = [
    path('', views.teacher_login,name="teacherlogin"),
    path('TeacherDashboard/', views.teacher_dash,name='teacherdash'),
    path('TeacherQuestion/', views.teacher_question,name='teacherquestion'),
    path('TeacherAddQuestion/',views.teacher_add_question,name='teacheraddquestion'),
    path('TeacherProfile/', views.teacher_profile,name='teacherprofile'),
]
