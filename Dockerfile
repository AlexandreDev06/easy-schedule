FROM python:3.12-slim AS builder

RUN pip install poetry==1.8.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache
WORKDIR /poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

FROM python:3.12-slim AS runtime

ENV VIRTUAL_ENV=/poetry/.venv \
    PATH="/poetry/.venv/bin:$PATH" \
    TZ=America/Sao_Paulo

RUN pip install poetry==1.8.2

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

WORKDIR /home/app

COPY . .

EXPOSE 8000

CMD ["sh", "entrypoint.sh"]