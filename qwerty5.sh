#!/bin/bash

# Проверяем, установлен ли Docker
if ! command -v docker &> /dev/null; then
    echo "Docker не установлен. Установите Docker и повторите попытку."
    exit 1
fi

# Проверяем, существует ли контейнер с именем "nginx-container"
if docker ps -a --format '{{.Names}}' | grep -q '^nginx-container$'; then
    # Останавливаем и удаляем существующий контейнер
    docker stop nginx-container
    docker rm nginx-container
    echo "Старый контейнер 'nginx-container' был остановлен и удален."
fi

# Создаем и запускаем новый контейнер с обновленным образом Nginx
docker run -d --name nginx-container -p 8080:80 nginx
echo "Новый контейнер 'nginx-container' был создан и запущен на порту 8080."

