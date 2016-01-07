
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    office_number = models.CharField(max_length=7)
    email = models.EmailField()
    phone = models.IntegerField()

class Course(models.Model):
    c_classroom = models.CharField(max_length=50)
    c_time = models.CharField(max_length=50)
    c_teacher = models.OneToOneField(Teacher)
    c_students = models.ManyToManyField(Student)
    c_code = models.CharField(max_length=7)
