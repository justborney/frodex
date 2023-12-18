FROM python:3.10-alpine

ENV APP_HOME=frodex_likes/backend

RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip

COPY . $APP_HOME/

RUN pip3 install -r $APP_HOME/requirements.txt

COPY . .
COPY .env .

RUN mkdir -p /logs
RUN echo "." > logs/celery.log