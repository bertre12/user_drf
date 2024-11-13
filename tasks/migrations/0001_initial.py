# Generated by Django 5.1.1 on 2024-11-13 19:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_task', models.CharField(max_length=255, verbose_name='Название задания')),
                ('type_task', models.CharField(choices=[('задание', 'задание'), ('опрос', 'опрос')], max_length=100, verbose_name='Тип задания')),
                ('description', models.CharField(max_length=255, verbose_name='Описание задания')),
                ('detailed_description', models.CharField(max_length=255, verbose_name='Подробное описание задания')),
                ('points_task', models.PositiveIntegerField(default=0, verbose_name='Кол-во баллов за задание')),
                ('fill_profile', models.CharField(choices=[('Никнейм Instagram', 'Никнейм Instagram'), ('Ничего', 'Ничего')], max_length=100, verbose_name='Заполнение профиля')),
                ('open_time_task', models.PositiveIntegerField(default=0, verbose_name='Через сколько времени откроется задание')),
                ('number_classes', models.PositiveIntegerField(default=0, verbose_name='Через сколько занятий откроется задание')),
                ('students', models.ManyToManyField(related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='Студенты')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
    ]