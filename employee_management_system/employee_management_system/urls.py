from django.contrib import admin
from django.urls import path, include
from .views import home, login_user, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('employees/', include('employees.urls')),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),


]
