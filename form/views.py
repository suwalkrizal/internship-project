# form/views.py
from django.shortcuts import render, get_object_or_404, redirect
from student.models import *
from .forms import *
from django.urls import reverse

def student_list(request):
    students = Student.objects.all()
    return render(request, 'form/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('student_list'))
    else:
        form = StudentForm()
    return render(request, 'form/student_form.html', {'form': form})

def student_update(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect(reverse('student_list'))
    else:
        form = StudentForm(instance=student)
    return render(request, 'form/student_form.html', {'form': form})

def student_delete(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect(reverse('student_list'))
    return render(request, 'form/student_delete.html', {'student': student})
