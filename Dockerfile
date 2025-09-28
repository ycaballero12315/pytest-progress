FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


ENV PATH="/root/.cargo/bin:$PATH"


COPY pyproject.toml ./


RUN uv pip install --system -e .


COPY . .


CMD ["pytest", "-v"]