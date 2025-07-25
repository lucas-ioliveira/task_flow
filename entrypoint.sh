#!/bin/bash

echo "Aguardando o banco de bados..."
sleep 5

echo "Verificando migrações para o banco de bados..."
python manage.py migrate
sleep 5

echo "Aplicando migrações para o banco de bados..."
python manage.py migrate
sleep 5

echo "Iniciando o servidor Django"
python manage.py runserver 0:8003