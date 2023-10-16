# Используем образ с Python
FROM python:3.8

# Устанавливаем зависимости
RUN pip install flask psycopg2

# Копируем код приложения в контейнер
COPY . /app
WORKDIR /app

# Запускаем приложение
CMD ["python", "app.py"]
