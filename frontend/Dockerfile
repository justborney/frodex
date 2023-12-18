FROM node:20-alpine as builder

ENV APP_HOME=/frodex_likes/frontend

RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

COPY ./package*.json $APP_HOME/

RUN npm install

COPY . $APP_HOME/

CMD ["npm","start"]
