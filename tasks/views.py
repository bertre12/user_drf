from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from student.models import Student
from .serializers import TaskSerializer, ListTaskSerializer
import logging

# Создание логгера.
logger = logging.getLogger(__name__)


# Вывод задания.
class TaskDetailView(APIView):
    def get(self, request, pk):
        # Запрос по id заданию.
        try:
            # При верном запросе.
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task)

            # Добавление логгера.
            logger.info(f'Вывод задания - {task.name_task} и его ID {task.id}.')
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            # Задание не найдено при неверном запросе.
            # Добавление логгера.
            logger.error(f'Задание с ID {pk} не найдено!')
            return Response({'error': 'Task not found'},
                            status=status.HTTP_404_NOT_FOUND)


# Вывод списка заданий по пользователю.
class StudentTasksView(APIView):
    def get(self, request, student_id):
        # Получение id студента.
        try:
            student = Student.objects.get(id=student_id)

            # Добавление логгера.
            logger.info(f'Вывод списка заданий для студента {student.name}.')
        except Student.DoesNotExist:

            # Добавление логгера.
            logger.error(f'Студент с ID {student_id} не найден!')
            return Response({'error': 'Student not found'},
                            status=status.HTTP_404_NOT_FOUND)

        # Фильтр заданий по студенту.
        tasks = Task.objects.filter(students=student)

        # Добавление логгера.
        logger.info(f'Найдено заданий для студента {student.name} в '
                    f'количестве - {tasks.count()}.')

        # Сериализация заданий.
        serializer = ListTaskSerializer(tasks, many=True)

        # Формирование ответа на запрос.
        response_data = {
            'student_name': student.name,
            'student_image': request.build_absolute_uri(
                student.image.url) if student.image else None,
            'tasks': serializer.data
        }
        # Отображения списка заданий.
        return Response(response_data, status=status.HTTP_200_OK)
