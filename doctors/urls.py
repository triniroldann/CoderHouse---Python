from django.contrib import admin
from django.urls import path
from doctors.views import create_doctor, update_doctor, Doctors_list,DoctorDeleteView

urlpatterns = [
    path('newdoctor/', create_doctor),
    path('list-doctors/', Doctors_list.as_view()),
    path('doctor-update/<int:id>', update_doctor),
   path('doctor-delete/<int:pk>', DoctorDeleteView.as_view()),

    path('admin/', admin.site.urls),
]