from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id','first_name','last_name','address','age','contact','email','grade','major')
    search_fields = ('first_name','student_id','contact','major')
    list_per_page = 10