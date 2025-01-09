from rest_framework import generics
from .serializers import StudentSerializer
from student.models import Student
import logging

# Создание логгера.
logger = logging.getLogger(__name__)


# Отображение всех студентов и их баллов.
class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Добавление логгера.
    def get(self, request, *args, **kwargs):
        logger.info('Запрошен список студентов.')
        return super().get(request, *args, **kwargs)


# Отображение баллов определенного студента.
class StudentDetailView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # Поиск студента по id.
    lookup_field = 'id'

    def get_object(self):
        # Переопределение метода для использования больше логики.
        obj = super().get_object()
        # Включение дополнительной операции, если это нужно.
        # Добавление логгера.
        logger.info(f'Список баллов для студента {obj.name}.')
        return obj
