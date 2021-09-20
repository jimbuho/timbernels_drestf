FROM python:3

ENV PYTHONNUMBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY requirements/requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/