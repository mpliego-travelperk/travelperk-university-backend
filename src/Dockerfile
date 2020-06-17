FROM python:3.7-alpine
MAINTAINER Martin Pliego.

# Default envirorment variables
ENV PYTHONUNBUFFERED 1
ENV DB_PATH "/data/db.sqlite3"

# Install dependencies
RUN apk add make
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY . /app

# Asume non-root identity
RUN adduser -D user
RUN mkdir /data
RUN chown user /data
USER user

VOLUME ["/data"]

ENTRYPOINT ["make"]
CMD ["run"]