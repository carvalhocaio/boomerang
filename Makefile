run:
	python manage.py runserver

lint:
	ruff check . && ruff check . --diff

format:
	ruff check . --fix && ruff format .