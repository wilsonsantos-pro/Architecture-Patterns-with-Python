FROM python:3.9-slim-buster

# RUN apt install gcc libpq (no longer needed bc we use psycopg2-binary)

RUN mkdir -p /app /src /local_dist
COPY src/ /app/src/
COPY pyproject.toml /app/
COPY tests/ /app/tests/
COPY local_dist/ /app/local_dist/

WORKDIR /app/src

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
