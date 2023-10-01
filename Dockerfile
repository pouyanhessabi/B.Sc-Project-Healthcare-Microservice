FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./ .
