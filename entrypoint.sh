#!bin/bash

echo "Aguardando o banco de bados..."
sleep 5

echo "Iniciando o servidor Django"
python manage.py runserver 0:8003