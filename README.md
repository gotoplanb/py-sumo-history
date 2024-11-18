# py-sumo-history
An application to ingest and manage Sumo Logic history


## Running

`make run`

## Testing

### Send an alert and see the message

`curl -X POST "http://127.0.0.1:8000/alert" -H "Content-Type: application/json" -d '{"message": "This is a test alert"}' | jq`
`curl -X POST "http://127.0.0.1:8000/alert" -H "Content-Type: application/json" -d '{"message": "{\"type\":\"critical\",\"environment\":\"prod\"}"}' | jq`
