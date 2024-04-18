FROM python:3.11-alpine

WORKDIR /jubellos_api/

# Install system dependencies
RUN apk add --no-cache \
    curl \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    bash

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /jubellos_api/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --only main ; fi"

ENV PYTHONPATH=/jubellos_api

COPY ./jubellos_api /jubellos_api/jubellos_api

CMD ["uvicorn", "jubellos_api.app:app", "--host", "0.0.0.0", "--port", "1337"]