# UUID Generator API

A simple FastAPI project that generates unique UUIDs.  
Supports multiple options such as count, version, prefix, and format.

## Features
- Generate one or more UUIDs
- Choose between UUID v1 (time-based) or v4 (random)
- Optional prefix for each UUID
- Short or full format output

## Installation
```bash
python -m venv .venv
.venv\Scripts\activate
pip install fastapi uvicorn
```

### Run the server:
uvicorn main:app --reload

### Usage:
Open http://127.0.0.1:8000/docs in your browser and test the endpoints.

Example Requests:
/generate → one random UUID
/generate?count=5 → five UUIDs
/generate?count=3&version=1 → UUID version 1

/generate?count=3&prefix=user&format=short → prefixed short IDs
