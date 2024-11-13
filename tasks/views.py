from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from student.models import Student
from .serializers import TaskSerializer, ListTaskSerializer


# Вывод задания.
class TaskDetailView(APIView):
    def get(self, request, pk):
        # Запрос по id заданию.
        try:
            # При верном запросе.
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:

            # Задание не найдено при неверном запросе.
            return Response({'error': 'Task not found'},
                            status=status.HTTP_404_NOT_FOUND)


# Вывод списка заданий по пользователю.
class StudentTasksView(APIView):
    def get(self, request, student_id):
        # Получение id студента.
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'},
                            status=status.HTTP_404_NOT_FOUND)

        # Фильтр заданий по студенту.
        tasks = Task.objects.filter(students=student)

        # Сериализация заданий.
        serializer = ListTaskSerializer(tasks, many=True)

        # Формирование ответа на запрос.
        response_data = {
            'student_name': student.name,
            'tasks': serializer.data
        }

        # Отображения списка заданий.
        return Response(response_data, status=status.HTTP_200_OK)
