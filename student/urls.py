from django.urls import path

from student.views import LoginView, StudentUpdateView, StudentCreateView, \
    LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  # Вход в систему для
    # пользователей student из бд Student.
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', StudentCreateView.as_view(), name='create-student'),
    # Регистрация нового пользователя student в бд Student.
    path('update/<int:pk>/', StudentUpdateView.as_view(),
         name='update-student'),  # Редактирование данных пользователя
    # student в бд Student.
]