from rest_framework import generics
from .serializers import StudentSerializer
from student.models import Student


# Отображение всех студентов и их баллов.
class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


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
        return obj
