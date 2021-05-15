from django.urls import path
from . import views


urlpatterns = [
    path('', views.teacher_login,name="teacherlogin"),
    path('TeacherDashboard/', views.teacher_dash,name='teacherdash'),
    path('TeacherAddQuestion/',views.teacher_add_question,name='teacheraddquestion'),
    path('TeacherProfile/', views.teacher_profile,name='teacherprofile'),
    path('QuestionDelete/<int:id>', views.teacher_delete_question,name='questiondelete'),
    path('QuestionEdit/<int:id>', views.teacher_edit_question,name='questionedit'),
]
