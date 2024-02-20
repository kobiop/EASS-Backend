# Frontend Dockerfile
FROM python:3.9

WORKDIR /app

COPY frontend_requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py app.py

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
