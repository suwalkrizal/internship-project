# form/urls.py
from django.urls import path
from .views import student_list, student_create, student_update, student_delete

urlpatterns = [
    path('', student_list, name='student_list'),
    path('create/', student_create, name='student_create'),
    path('update/<int:student_id>/', student_update, name='student_update'),
    path('delete/<int:student_id>/', student_delete, name='student_delete'),
]
