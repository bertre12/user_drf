from django.db import models


# Создание таблицы заданий.
class Task(models.Model):
    TYPE_CHOICES = [
        ('задание', 'задание'),
        ('опрос', 'опрос'),
    ]
    FILL_CHOICES = [
        ('Никнейм Instagram', 'Никнейм Instagram'),
        ('Ничего', 'Ничего'),
    ]
    # Связь многие ко многим.
    students = models.ManyToManyField('student.Student', related_name='tasks',
                                      verbose_name='Студенты')
    name_task = models.CharField(max_length=255,
                                 verbose_name='Название задания')
    type_task = models.CharField(max_length=100, verbose_name='Тип задания',
                                 choices=TYPE_CHOICES)
    description = models.CharField(max_length=255,
                                   verbose_name='Описание задания')
    detailed_description = models.CharField(max_length=255,
                                            verbose_name='Подробное описание задания')
    points_task = models.PositiveIntegerField(default=0,
                                              verbose_name='Кол-во баллов за задание')
    fill_profile = models.CharField(max_length=100,
                                    verbose_name='Заполнение профиля',
                                    choices=FILL_CHOICES)
    open_time_task = models.PositiveIntegerField(default=0,
                                                 verbose_name='Через сколько времени откроется задание')
    number_classes = models.PositiveIntegerField(default=0,
                                                 verbose_name='Через сколько занятий откроется задание')

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return f'{self.name_task} ({self.type_task})'
