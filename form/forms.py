from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name','address','age','contact','email']
