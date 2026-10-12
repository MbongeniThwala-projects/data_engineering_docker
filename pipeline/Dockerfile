FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
#this syncs our dependencies in our uv.lockk file (must be the same as those in our VM)

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked

COPY pipeline.py .

ENTRYPOINT ["python", "pipeline.py"]