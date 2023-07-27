# behavior_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_page, name='default_page'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),



]
