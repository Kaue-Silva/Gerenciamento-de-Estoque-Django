FROM python:3.10.4-alpine

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1 

WORKDIR /code

RUN apk add git gpg gnupg gpg-agent socat

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .