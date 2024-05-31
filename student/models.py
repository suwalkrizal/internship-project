from django.db import models

# Create your models here.

class Student(models.Model):
    choice =[
        ('IT', 'B.Sc.CSIT'),
        ('Engineer', 'Computer Engineer'),
        ('Engineer', 'Civil Engineer'),
        ('Engineer', 'Electronic Engineer'),
    ]
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    age = models.IntegerField()
    contact = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=30)
    grade =models.CharField(max_length=20)
    major = models.CharField(max_length=20, choices=choice)
    
    def __str__(self):
        return f"{self.student_id}-{self.first_name}-{self.last_name}-{self.major}"

