from django.db import models

# Create your models here.

class Teacher(models.Model):
    full_name = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    clas = models.ManyToManyField('Class')


class Class(models.Model):
    name = models.CharField(max_length=50)


class Student(models.Model):
    full_name = models.CharField(max_length=70)
    clas = models.ForeignKey(Class,on_delete=models.CASCADE)