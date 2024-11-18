from fastapi import FastAPI
from pydantic import BaseModel
import json
import asyncpg
import os

app = FastAPI()

class Alert(BaseModel):
    message: str

# Get database connection settings from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://username:password@localhost/sumo")

async def init_db():
    """Initialize the database connection."""
    app.state.db = await asyncpg.create_pool(DATABASE_URL)

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.on_event("shutdown")
async def shutdown_event():
    await app.state.db.close()

@app.post("/alert")
async def create_alert(alert: Alert):
    try:
        # Parse the message as JSON, if applicable
        parsed_message = json.loads(alert.message)
    except json.JSONDecodeError:
        parsed_message = alert.message

    # Print the message to stdout
    print(parsed_message)

    # Save the alert to the database
    async with app.state.db.acquire() as connection:
        await connection.execute(
            "INSERT INTO alerts (message) VALUES ($1)",
            alert.message
        )

    return {"status": "Alert received", "message": parsed_message}
