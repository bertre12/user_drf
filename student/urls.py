from django.urls import path

from student.views import CreateUserView, UserList, UserDelete, LoginView, \
    StudentUpdateView, StudentCreateView, LogoutView

urlpatterns = [
    # path('create_user/', CreateUserView.as_view(), name='create_user'),
    # # Создание нового пользователя.
    # path('users/', UserList.as_view(), name='user_list'),  # Список
    # # пользователей.
    # path('users/<int:pk>/', UserDelete.as_view(), name='user_editing'),
    # # Редактирование и удаление пользователя по id.
    path('login/', LoginView.as_view(), name='login'),  # Вход в систему для
    # пользователей student из бд Student.
    path('logout/', LogoutView.as_view(), name='logout'),
    path('students/', StudentCreateView.as_view(), name='create-student'),
    # Регистрация нового пользователя student в бд Student.
    path('students/<int:pk>/', StudentUpdateView.as_view(),
         name='update-student'),  # Редактирование данных пользователя
    # student в бд Student.
]