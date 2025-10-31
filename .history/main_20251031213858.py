from fastapi import FastAPI, Query
import uuid

app = FastAPI(title="UUID Generator API", version="2.0.0")

@app.get("/")
def home():
    return {
        "message": "Welcome to UUID Generator API!",
        "usage_example": "/generate?count=5&version=4&prefix=test&format=short"
    }

@app.get("/generate")
def generate_uuids(
    count: int = Query(default=1, ge=1, le=100, description="How many UUIDs to generate"),
    version: int = Query(default=4, ge=1, le=5, description="UUID version: 1 (time-based) or 4 (random)"),
    prefix: str = Query(default="", description="Optional prefix to add before each UUID"),
    format: str = Query(default="full", description="Output format: 'full' or 'short'")
):
    uuids = []

    for _ in range(count):
        if version == 1:
            uid = uuid.uuid1()
        else:
            uid = uuid.uuid4()

        if format == "short":
            uid_str = uid.hex[:8]
        else:
            uid_str = str(uid)

        # prefix
        if prefix:
            uid_str = f"{prefix}_{uid_str}"

        uuids.append(uid_str)

    return {
        "count": count,
        "version": version,
        "prefix": prefix or None,
        "format": format,
        "uuids": uuids
    }
