from django.shortcuts import render
from .models import Teacher,Student
# Create your views here.

from rest_framework import viewsets
from .serializers import TeacherSerializer,StudentSerializer


class TeacherApiViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentApiViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer