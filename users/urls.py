from django.contrib import admin
from django.urls import path
from users.views import login_view,register, update_user,update_user_profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name= 'login'),
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html')),
    path('register/',register, name= 'register'),
    path('update-user/', update_user, name= 'update-user'),
    path('update-profile/', update_user_profile, name = 'update_user_profile')
]