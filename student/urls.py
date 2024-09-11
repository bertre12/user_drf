from django.urls import path

from student.views import CreateUserView, UserList, UserDelete

urlpatterns = [
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    # Создание нового пользователя.
    path('users/', UserList.as_view(), name='user_list'),  # Список
    # пользователей.
    path('users/<int:pk>/', UserDelete.as_view(), name='user_editing'),
    # Редактирование и удаление пользователя по id.
]