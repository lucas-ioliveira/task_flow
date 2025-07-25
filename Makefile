DJANGO = python manage.py

runserver:
	$(DJANGO) runserver 0:8003

makemigrations:
	$(DJANGO) makemigrations

migrate:
	$(DJANGO) migrate

test:
	$(DJANGO) test

requirements:
	pip freeze > requirements.txt

format:
	flake8

build:
	docker compose -f docker-compose.yml up -d --build

