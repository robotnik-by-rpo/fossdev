FROM python:3.12-slim
WORKDIR /app

COPY pyproject.toml poetry.load ./
RUN pip install poetry && poetry install --only main --no_root

COPY src/app ./app

CMD ["poetry","run", "uvicorn", "app.main:app", "--host",\
    "0.0.0.0", "--post","8000"]