from django.apps import AppConfig


class StudentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student'

    # Корректное отображение в админпанели.
    verbose_name = 'Студент'
