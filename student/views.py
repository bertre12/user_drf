from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .models import Student
from .serializers import UserSerializer, LoginSerializer, \
    StudentUpdateSerializer, StudentRegisterSerializer
from rest_framework.response import Response


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
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.validated_data['student']
        # Информация после входа в систему.
        return Response({'message': f'Вы вошли как {student.name}'})


# Добавление нового пользователя student в таблице Student.
class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentRegisterSerializer


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
