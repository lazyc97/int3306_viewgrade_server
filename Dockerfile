# Database
FROM mongo:4-xenial AS database
COPY ./conf/DbInit.js /docker-entrypoint-initdb.d/DbInit.js
COPY ./conf/DbDummyGen.js /tools/DbDummyGen.js

# API server
FROM nginx:alpine AS api_server_dev
RUN apk add --no-cache python3

WORKDIR /app
COPY ./tornado/requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

RUN mkdir -p /storage/pdf
CMD nginx && python3 main.py

FROM api_server_dev AS api_server_prod
COPY ./tornado /app
COPY ./conf/nginx.conf /etc/nginx/nginx.conf
