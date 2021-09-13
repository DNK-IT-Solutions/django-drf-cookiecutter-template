FROM dnkitsolutions/meinheld-gunicorn:python3.9-alpine3.13

ENV MODULE_NAME=main.wsgi
ENV VARIABLE_NAME=application

RUN apk --virtual .build-deps add gcc musl-dev libffi-dev openssl-dev postgresql-dev
RUN apk add libpq gettext


RUN CRYPTOGRAPHY_DONT_BUILD_RUST=1 python -m pip install poetry

COPY ./pyproject.toml /app/
COPY ./poetry.lock /app/

RUN python -m poetry config virtualenvs.create false


COPY ./src /app

RUN poetry install --no-dev

RUN apk --purge del .build-deps

COPY ./scripts/prestart.sh /app/
