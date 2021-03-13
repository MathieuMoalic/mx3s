# pull official base image
FROM python:3.9.2-alpine

# set work directory
WORKDIR /usr/src/jimmy/ftp

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install pyftpdlib

# copy project
COPY . .
