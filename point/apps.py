from django.apps import AppConfig


class PointConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'point'

    # Корректное отображение в админпанели.
    verbose_name = 'Задание'
