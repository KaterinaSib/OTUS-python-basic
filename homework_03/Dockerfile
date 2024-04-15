FROM python:3.12-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip poetry==1.8.2

RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN poetry install --only main

COPY my_new_app ./

CMD ["uvicorn", "app:app", "--host", "localhost", "--port", "8000"]
