db-up:
	docker-compose --file docker/docker-compose.yml up -d

db-down:
	docker-compose --file docker/docker-compose.yml down

init-db:
	python init-tables.py

test:
	pytest

flask-run:
	export FLASK_APP=app.py
	flask run