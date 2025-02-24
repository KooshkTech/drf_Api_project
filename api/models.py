from django.db import models # type: ignore

# Create your models here.
from django.db import models # type: ignore

class Student(models.Model):  
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Employee(models.Model):
    emp_id = models.CharField(max_length=20)
    emp_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.emp_name
