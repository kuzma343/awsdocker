#!/bin/bash
# Проверяем, установлен ли Docker
if ! command -v docker &> /dev/null; then
    echo "Docker не установлен. Установите Docker и повторите попытку."
    exit 1
fi

# Проверяем, запущен ли контейнер с именем "nginx-container"
if docker ps --format '{{.Names}}' | grep -q '^nginx-container$'; then
    # Останавливаем контейнер
    docker stop nginx-container
    echo "Контейнер 'nginx-container' был остановлен."
else
    echo "Контейнер с именем 'nginx-container' не запущен."
fi

