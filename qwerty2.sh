#!/bin/bash

# Проверяем, установлен ли Docker
if ! command -v docker &> /dev/null; then
    echo "Docker не установлен. Установите Docker и повторите попытку."
    exit 1
fi

# Проверяем, запущен ли контейнер с именем "nginx-container"
if docker ps -a --format '{{.Names}}' | grep -q '^nginx-container$'; then
    echo "Контейнер с именем 'nginx-container' уже существует и может быть запущен."
else
    # Создаем и запускаем контейнер с Nginx, привязывая его к порту 8080
    docker run -d --name nginx-container -p 8080:80 nginx
    echo "Контейнер 'nginx-container' был создан и запущен на порту 8080."
fi

