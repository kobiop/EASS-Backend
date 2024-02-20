# Backend Dockerfile
FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r backend_requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
