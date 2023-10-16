# Используем официальный образ PostgreSQL
FROM postgres:latest
# Копируем скрипт миграции в контейнер
COPY init.sql /docker-entrypoint-initdb.d/
