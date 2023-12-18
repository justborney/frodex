FROM node:20-alpine as builder

ENV APP_HOME=/usr/src/frodex_likes/frontend

RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

COPY . $APP_HOME/

RUN npm install

CMD ["npm", "run", "start"]