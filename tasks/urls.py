from django.urls import path
from .views import TaskDetailView, StudentTasksView

urlpatterns = [
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    # Отображение информации о задании.
    path('list/<int:student_id>/', StudentTasksView.as_view(),
         name='student-tasks'),  # Вывод списка заданий для студента.
]