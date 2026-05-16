# Используем легкий образ Python
FROM python:3.11-slim

# Устанавливаем переменные окружения для предотвращения создания .pyc файлов и буферизации вывода
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем системные зависимости, необходимые для сборки некоторых пакетов
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь код проекта в контейнер
COPY . .

# Собираем статические файлы (если в settings.py настроен STATIC_ROOT)
# Если команда collectstatic не нужна, её можно закомментировать или убрать
RUN python manage.py collectstatic --noinput --clear || true

# Открываем порт, на котором будет работать приложение (по умолчанию 8000)
EXPOSE 8000

# Команда для запуска сервера (используем gunicorn для production-like среды)
# Если gunicorn не установлен в requirements.txt, можно заменить на:
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wp_labs.wsgi:application"]
