FROM python:3.12-slim-bullseye

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBEFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# RUN apt update -y && apt upgrade -y 
RUN chmod +x ./setup.sh
RUN ./setup.sh
