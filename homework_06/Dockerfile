FROM tiangolo/uwsgi-nginx:python3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /my_app

RUN pip install --upgrade pip poetry==1.8.2

RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN poetry install --only main

COPY ./prestart.sh ./prestart.sh

COPY my_app ./