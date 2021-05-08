from django.urls import path
from . import views
from MCQ_Test import views


urlpatterns = [
    path('', views.home_page,name="Exampath"),
    path('ContactUs/', views.contact_us,name="Contactpath"),
    path('AdminWeb/', views.admin_web,name="Adminpath"),


]
