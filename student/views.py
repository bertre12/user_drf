from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import UserSerializer


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
