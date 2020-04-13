FLASK_APP=http_api
FLASK_ENV=development
HOST?="0.0.0.0"
PORT?=8080

init: requirements.txt
	pip install -r $<

dev:
	FLASK_APP=${FLASK_APP} FLASK_ENV=${FLASK_ENV} python -m flask run --host ${HOST} --port ${PORT}

.PHONY = init dev
