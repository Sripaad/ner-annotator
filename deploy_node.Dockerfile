FROM node:14.16-buster-slim

COPY ./ui /app
WORKDIR /app/ui

RUN yarn install

CMD ["yarn", "serve"]