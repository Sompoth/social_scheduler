from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import os

from database import add_post, get_posts
from ai_utils import generate_caption, generate_image

# Initialize FastAPI
app = FastAPI()

# Pydantic model for requests
class PostRequest(BaseModel):
    content: str
    scheduled_time: str  # Format: YYYY-MM-DD HH:MM

@app.post("/schedule/")
def schedule_post(request: PostRequest):
    """Schedule a social media post."""
    try:
        datetime.strptime(request.scheduled_time, "%Y-%m-%d %H:%M")
        add_post(request.content, request.scheduled_time)
        return {"message": "Post scheduled successfully!"}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid datetime format. Use YYYY-MM-DD HH:MM")

@app.get("/posts/")
def get_scheduled_posts():
    """Retrieve all scheduled posts."""
    return {"posts": get_posts()}

@app.post("/generate_caption/")
def caption_generator(topic: str):
    """Generate a social media caption based on a topic."""
    return {"caption": generate_caption(topic)}

@app.post("/generate_image/")
def image_generator(prompt: str):
    """Generate an AI image using DALL·E based on user input."""
    return {"image_url": generate_image(prompt)}
