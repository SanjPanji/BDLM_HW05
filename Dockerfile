FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
COPY prime_pack_spanji/ ./prime_pack_spanji/

RUN pip install --no-cache-dir .

ENTRYPOINT ["python", "-m", "prime_pack_spanji"]
