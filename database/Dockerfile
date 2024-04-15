# Use the official Docker Hub Postgres image
FROM postgres

# Set environment variables
ARG POSTGRES_USER
ENV POSTGRES_USER=$POSTGRES_USER

ARG POSTGRES_PASSWORD
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD

ARG POSTGRES_DB
ENV POSTGRES_DB=$POSTGRES_DB

# Copy the SQL script into the docker-entrypoint-initdb.d directory
COPY create-data.sql /docker-entrypoint-initdb.d/