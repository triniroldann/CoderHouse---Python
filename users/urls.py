from django.contrib import admin
from django.urls import path
from users.views import login_view,register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view),
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html')),
    path('register/',register)
]