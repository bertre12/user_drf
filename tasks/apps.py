from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

    # Корректное отображение в админпанели.
    verbose_name = 'Задания'
