FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /web/requirements.txt
RUN pip install --no-cache-dir --disable-pip-version-check -r /web/requirements.txt

ADD     https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /web/wait
RUN     chmod +x /web/wait

WORKDIR /web

COPY . /web