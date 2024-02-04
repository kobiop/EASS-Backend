from python:3.8.10

WORKDIR /app

copy . /app

RUN pip install -r requirements.txt