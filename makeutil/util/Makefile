include .env
export

run-pip:
	$(PIP) install -e .

run-req:
	$(PIP) install pytest
install-req:
	$(PIP) install requests

pytest: install-req run-req
	.venv/bin/pytest ./tests/test_util.py
