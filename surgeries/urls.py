from django.contrib import admin
from django.urls import path
from surgeries.views import list_surgeries, create_surgerie,create_category,list_categories


urlpatterns = [
    path('newsurgerie/',create_surgerie),
    path('list-surgeries/',list_surgeries),
    path('newcategory/<str:name>', create_category),
    path('list-categories/', list_categories),


    path('admin/', admin.site.urls),
]