PY_ENV = venv/bin/python

venv:
	virtualenv -p python3.5 venv
	venv/bin/pip install -r requirements.txt

server:
	$(PY_ENV) src/manage.py runserver

fixtures:
	$(PY_ENV) src/manage.py loaddata initial.core.json
	$(PY_ENV) src/manage.py loaddata initial.adverts.json

user:
	$(PY_ENV) src/manage.py createsuperuser

migrate:
	$(PY_ENV) src/manage.py migrate

start:
	make venv \
	migrate \
	fixtures \
	user \
	server
