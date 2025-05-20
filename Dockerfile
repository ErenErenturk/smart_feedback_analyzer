FROM python:3.10

WORKDIR /app

COPY . .
COPY .env .env

ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--log-level", "debug"]

EXPOSE 8000
