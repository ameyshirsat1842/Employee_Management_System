from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('<int:pk>/', views.employee_detail, name='employee_detail'),
    path('new/', views.employee_create, name='employee_create'),
    path('<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    path('<int:employee_id>/leave-records/new/', views.leave_record_create, name='leave_record_create'),
    path('<int:employee_id>/leave-records/<int:record_id>/edit/', views.leave_record_update, name='leave_record_update'),
    path('<int:employee_id>/leave-records/<int:record_id>/delete/', views.leave_record_delete, name='leave_record_delete'),
    path('register/', register, name='register')

]
