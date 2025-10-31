from fastapi import FastAPI, Query
import uuid

app = FastAPI(title="UUID Generator API", version = "1.0.0")

@app.get("/")
def home():
    return{
        "message": "Welcome to UUID Generator API",
        "example_usage": "/generate?count=5"
    }
    
@app.get("/home")
def generate_uuuids(count: int = Query(default=1, ge=1, le=100, description="How many UUIDs to generate")):
    ids = [str(uuid.uuid4()) for _ in range(count)]
    return {"count": count, "uuids": ids}