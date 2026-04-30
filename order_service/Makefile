create-structure:
	mkdir src tests docs
	touch README.md setup.py requirements.txt
	touch docs/DOMAIN.md docs/SPECIFICATION.md
	touch src/.gitkeep tests/.gitkeep

install-dep:
	pip install -r requirements.txt

install:
	pip install -e .

test-pytest:
	python3 -m pytest

test: install-dep install test-pytest


HOST ?= 127.0.0.1
PORT ?= 8001

run-p:
	cd .. && cd product_service && poetry run uvicorn src.app.main:app --host ${HOST} --port ${PORT}

run-o:
	export PRODUCT_SERVICE_URL && poetry run uvicorn src.app.main:app --host ${HOST} --port 8002

run:
	make -j2 run-o run-p