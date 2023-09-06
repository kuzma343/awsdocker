#!/bin/bash

# Проверяем, установлен ли Docker
if ! command -v docker &> /dev/null; then
    echo "Docker не установлен. Установите Docker и повторите попытку."
    exit 1
fi

# Проверяем, существует ли контейнер с именем "nginx-container"
if docker ps -a --format '{{.Names}}' | grep -q '^nginx-container$'; then
    # Удаляем контейнер
    docker rm nginx-container
    echo "Контейнер 'nginx-container' был удален."
else
    echo "Контейнер с именем 'nginx-container' не существует."
fi

