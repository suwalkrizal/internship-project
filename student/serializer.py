from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'student_id',
            'first_name',
            'last_name',
            'address',
            'age',
            'contact',
            'email',
            'grade',
            'major'
        )
        model=Student