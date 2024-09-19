import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.db import models


# Создание таблицы уровней.
class Level(models.Model):
    LEVEL_CHOICES = [
        ('Студент', 'Студент'),
        ('Менеджер', 'Менеджер'),
        ('Учитель', 'Учитель'),
        ('Админ', 'Админ'),
    ]
    name = models.CharField(max_length=100, choices=LEVEL_CHOICES, unique=True,
                            verbose_name='Статус', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровень'


# Создание таблицы студент.
class Student(models.Model):
    STATUS_CHOICES = [
        ('Учится', 'Учится'),
        ('В академ. отпуске', 'В академ. отпуске'),
        ('Возврат', 'Возврат'),
        ('Закончил обучение', 'Закончил обучение'),
    ]

    name = models.CharField(max_length=255, verbose_name='ФИО')
    image = models.ImageField(upload_to='static/images/', null=True,
                              verbose_name='Фото')
    password = models.CharField(max_length=255, verbose_name='Пароль')
    phone = models.CharField(max_length=255, verbose_name='№ телефона',
                             help_text='+375_________')
    e_mail = models.EmailField(max_length=255,
                               verbose_name='Электронная почта')
    nickname_tg = models.CharField(max_length=255, null=True,
                                   verbose_name='Никнейм Telegram')
    nickname_inst = models.CharField(max_length=255, null=True,
                                     verbose_name='Никнейм Instagram')
    group_number = models.CharField(max_length=255, verbose_name='№ группы')
    number_of_points = models.IntegerField(default=0,
                                           verbose_name='Количество баллов')
    status = models.CharField(max_length=100, verbose_name='Статус',
                              choices=STATUS_CHOICES)
    package = models.CharField(max_length=255, null=True, blank=True,
                               verbose_name='Пакет')
    internship = models.CharField(max_length=255, verbose_name='Стажировка')
    session_id = models.UUIDField(default=uuid.uuid4, editable=False,
                                  unique=True,
                                  verbose_name='Идентификатор сессии')

    level = models.ForeignKey('Level', on_delete=models.CASCADE, null=True,
                              verbose_name='Статус')

    # Хеширование пароля при создании нового пользователя.
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.name
