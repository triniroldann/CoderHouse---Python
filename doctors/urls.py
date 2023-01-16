from django.contrib import admin
from django.urls import path
from doctors.views import create_doctor, list_doctors

urlpatterns = [
    path('newdoctor/', create_doctor),
    path('list-doctors/',list_doctors),


    path('admin/', admin.site.urls),
]