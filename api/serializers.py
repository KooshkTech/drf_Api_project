from rest_framework import serializers # type: ignore
from students.models import Student
from employees.models import Employee# Import your models

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):  # ✅ Fixed here
    class Meta:
        model = Employee
        fields = '__all__'
