#!/bin/bash

# Оновлюємо інформацію про пакети
sudo apt-get update -y

# Встановлюємо Docker
sudo apt-get install -y docker.io

# Запускаємо Docker сервіс
sudo systemctl start docker

# Додаємо користувача до групи Docker, щоб не використовувати sudo для кожної команди Docker
sudo usermod -aG docker $USER

# Перезавантажуємо службу, щоб зміни вступили в силу
sudo systemctl restart docker

# Оновлюємо список пакетів та встановлюємо Git
sudo apt update
sudo apt install -y git

# Встановлюємо aiogram через pip3


# Встановлюємо Python 3 та pip3
sudo apt install -y python3 python3-pip

pip install aiogram==2.9.0
# Клонуємо ваш репозиторій
git clone https://github.com/kuzma343/awsdocker.git

# Переходимо в папку з клонованим репозиторієм
cd awsdocker/

# Надаємо права на виконання скриптів
chmod +x /awsdocker/qwerty.sh
chmod +x /awsdocker/qwerty2.sh
chmod +x /awsdocker/qwerty3.sh
chmod +x /awsdocker/qwerty4.sh
chmod +x /awsdocker/qwerty5.sh

# Виконуємо команду Python
python3 /awsdocker/bash.py
