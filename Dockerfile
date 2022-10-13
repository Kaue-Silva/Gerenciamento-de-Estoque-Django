FROM python:3.10.4-alpine

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1 

WORKDIR /code

RUN apk add git gpg gnupg gpg-agent socat
RUN git config --global --add safe.directory /code

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
