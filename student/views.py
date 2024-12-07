import uuid
from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .models import Student
from .permissions import IsOwner
from .serializers import StudentUpdateSerializer, StudentRegisterSerializer, \
    LoginSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


# Вход в систему пользователей student из таблицы Student.
class LoginView(generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.validated_data['student']

        # Генерация уникального session_id при входе и сохранение в бд.
        student.session_id = uuid.uuid4()
        student.save()

        # Сохранение информации о пользователе в сессии и его ID.
        request.session['student_id'] = student.id
        # Установка времени сессии (в секундах).
        request.session.set_expiry(600)
        session_time = 600

        # Информация после входа в систему.
        # Вы вошли в систему как
        return Response({'message': f'You are logged in as {student.name}',
                         'student.id': student.id,
                         'session_time': session_time})


# Добавление нового пользователя student в таблице Student.
class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentRegisterSerializer

    def perform_create(self, serializer):
        # Проверка на существование пользователя с таким же именем.
        name = serializer.validated_data['name']
        if Student.objects.filter(name=name).exists():
            # Пользователь с таким именем уже существует.
            raise ValidationError(
                {'name': 'A user with this name already exists.'})

        # Получаем данные.
        student = serializer.save()
        # Хэширование пароля.
        student.password = make_password(student.password)
        # Обновляем только поле пароля.
        student.save(update_fields=['password'])


# Редактирование пользователей student из таблицы Student.
class StudentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentUpdateSerializer
    permission_classes = [IsOwner]

    # Ограничение на редактирование только текущему пользователю.
    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return StudentRegisterSerializer
        elif self.request.method == 'PATCH':
            return StudentUpdateSerializer
        return super().get_serializer_class()


# Выход из системы.
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        student_id = request.session.get('student_id')

        if student_id:
            # Получение объекта студент.
            student = Student.objects.get(id=student_id)

            # Очистка session_id.
            student.session_id = None
            student.save()

            # Удаление информации о сессии и всех данных о пользователе.
            request.session.flush()

            # Вы вышли из системы.
            return Response({'message': 'You are logged out.'}, status=200)
        else:
            # Вы не авторизованы.
            return Response({'message': 'You are not authorized.'}, status=400)
