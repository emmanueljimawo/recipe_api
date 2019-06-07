FROM python:3.7-alpine
MAINTAINER Emmanuel Jimawo

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /recipe_api
WORKDIR /recipe_api
COPY ./recipe_app /recipe_api

RUN adduser -D user
USER user
