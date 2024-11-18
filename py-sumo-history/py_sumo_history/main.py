from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class Alert(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/alert")
def create_alert(alert: Alert):
    try:
        # Attempt to parse the message as JSON
        parsed_message = json.loads(alert.message)
    except json.JSONDecodeError:
        # If it's not valid JSON, keep it as a string
        parsed_message = alert.message

    print(parsed_message)  # Log the parsed message

    return {
        "status": "Alert received",
        "message": parsed_message
    }
