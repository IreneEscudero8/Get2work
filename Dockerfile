FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml README.md ./
COPY get2work/ ./get2work/
COPY sounds/ ./sounds/

RUN pip install -e .

RUN git init && git config user.email "demo@get2work.com" && git config user.name "get2work demo"

CMD ["get2work", "--help"]