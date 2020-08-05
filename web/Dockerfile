FROM node:latest

RUN apt update && apt install -yyq curl

RUN mkdir /opt/sennder-web
WORKDIR /opt/sennder-web

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./
COPY yarn.lock ./
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent

COPY . ./

EXPOSE 5000