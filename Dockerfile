FROM python:3.12-rc-slim-buster
LABEL mantainer="Lucas Oliveira"

WORKDIR /app
COPY . /app

EXPOSE 8003

RUN apt-get update && \
    apt-get install -y make pkg-config gcc default-libmysqlclient-dev python3-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip 
RUN pip install -r requirements

RUN chmod -R 777 /app
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]