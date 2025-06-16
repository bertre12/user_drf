# Создание облегченного образа.

# Базовый образ Python.
FROM python:3.10-slim

# Рабочая директория в контейнере.
WORKDIR /app

# Копируем зависимости и устанавливаем их.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Открываем порт для доступа.
EXPOSE 8000

# Команда для запуска сервера Django.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Создание  обычного образа.

## Используем официальный образ Python в качестве базового.
#FROM python:3.10-slim
#
## Устанавливаем рабочую директорию внутри контейнера.
#WORKDIR /app
#
## Копируем файлы проекта в контейнер.
#COPY . /app
#
## Устанавливаем зависимости.
#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt
#
## Открываем порт для доступа.
#EXPOSE 8000
#
## Команда для запуска сервера Django.
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]