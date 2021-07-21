db-up:
	docker-compose --file docker/docker-compose.yml up -d

db-down:
	docker-compose --file docker/docker-compose.yml down

test:
	pytest

flask-run:
	export FLASK_APP=app.py
	flask run