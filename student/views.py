from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .models import Student
from .serializers import UserSerializer, LoginSerializer, \
    StudentUpdateSerializer, StudentRegisterSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


# Создание нового пользователя для всех.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Отображение списка всех пользователей.
class UserList(generics.ListAPIView):  # Только чтение.
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Создание, редактирование и удаление после входа в систему.
class UserDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Добавление прав доступа.
    permission_classes = (IsAuthenticatedOrReadOnly,)


# Вход в систему пользователей student из таблицы Student.
class LoginView(generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.validated_data['student']

        # Сохранение информации о пользователе в сессии и его ID.
        request.session['student_id'] = student.id
        # Установка времени сессии (в секундах).
        request.session.set_expiry(120)
        session_time = 120

        # Информация после входа в систему.
        return Response({'message': f'Вы вошли как {student.name}',
                         'session_time': session_time})


# Добавление нового пользователя student в таблице Student.
class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentRegisterSerializer

    def perform_create(self, serializer):
        # Проверка на существование пользователя с таким же именем.
        if Student.objects.filter(
                name=serializer.validated_data['name']).exists():
            raise ValidationError(
                {"name": "Пользователь с таким именем уже существует."})

        # Получаем данные.
        student = serializer.save()
        # Хэширование пароля.
        student.password = make_password(student.password)
        student.save()


# Редактирование пользователей student из таблицы Student.
class StudentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentUpdateSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return StudentRegisterSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return StudentUpdateSerializer
        return super().get_serializer_class()
