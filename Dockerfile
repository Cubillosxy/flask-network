FROM python:3.7

MAINTAINER Edwin C
WORKDIR /tmp/

RUN apt-get update && apt-get install -y \
    vim \
    nano

RUN mkdir /code
WORKDIR /code
RUN easy_install -U pip
RUN pip install --upgrade pip

ADD requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt