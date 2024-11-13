from rest_framework import serializers
from .models import Task
from student.models import Student


# Вывод информации по заданию: кто его проходит и выборочная информация.
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # Поля отображения.
        fields = ['name']


class TaskSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['students', 'description', 'points_task']


# Вывод списка заданий по Студенту.
class ListTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # Поля отображения.
        fields = ['name_task', 'points_task', 'number_classes']
