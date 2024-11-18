# py-sumo-history
An application to ingest and manage Sumo Logic history.

Sumo Logic is fabulous at collecting, processing, and aggregates logs and metrics. It's not so great at sharing downstream. I have a need to send some data from Sumo Logic into Snowflake. Since there is no direct intregration, this application is a connector of sorts.

## Setup

### Create a local database container

1. Use Docker Hub for Mac.
1. Use the official Postgres image.
1. Set POSTGRES_PASSWORD variable.

### Create a database

```
CREATE DATABASE sumo;
```

### Create a database table

```
CREATE TABLE alerts (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Export connection string as environment variable

`export DATABASE_URL="postgresql://{your_user}:{your_password}@localhost/sumo"`

## Running

`make run`

## Testing

### Send alerts and see messages

1. String message: `curl -X POST "http://127.0.0.1:8000/alert" -H "Content-Type: application/json" -d '{"message": "This is a test alert"}' | jq`
1. JSON string message: `curl -X POST "http://127.0.0.1:8000/alert" -H "Content-Type: application/json" -d '{"message": "{\"type\":\"critical\",\"environment\":\"prod\"}"}' | jq`

### Query the database

`SELECT * FROM alerts;`