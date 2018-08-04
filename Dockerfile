# Database
FROM mongo:4-xenial AS database
COPY ./conf/db_init.js /docker-entrypoint-initdb.d/db_init.js

# API server
FROM nginx:alpine AS api_server_dev
RUN apk add --no-cache python3

WORKDIR /app
COPY ./tornado/requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

CMD nginx && python3 main.py

FROM api_server_dev AS api_server_prod
COPY ./tornado /app
COPY ./conf/nginx.conf /etc/nginx/nginx.conf
