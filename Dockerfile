FROM python:3.11-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y

RUN apt-get update && pip install -r requirements_dev.txt
CMD ["python3", "app.py"]