FROM node:14.2.0-alpine3.10

RUN npm install http-server -g
COPY html /html

WORKDIR /html
CMD http-server -p 8000 --cors
