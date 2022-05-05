FROM alpine:3.15
RUN apk update
RUN apk add \ 
php \ 
composer \
npm

WORKDIR /usr/local/apache2/htdocs

ADD . /usr/local/apache2/htdocs


EXPOSE 80