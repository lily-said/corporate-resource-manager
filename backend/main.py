"""
Employee Resource Manager - FastAPI backend.

Running:
    uvicorn main:app --reload --port 8000

Opening:
    http://127.0.0.1:8000/api/employees   -> the JSON data
    http://127.0.0.1:8000/docs            -> interactive API documentation
    http://127.0.0.1:8000/openapi.json    -> the generated JSON schema
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from mock_data import MOCK_EMPLOYEES
from models import Employee

app = FastAPI(
    title="Employee Resource Manager API",
    description="A small API that serves employee records.",
    version="0.1.0",
)

# Lets Angular (port 4200) call the API (port 8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # the Angular dev server
    allow_credentials=True,
    allow_methods=["*"],  # allow GET, POST, ...
    allow_headers=["*"],
)

@app.get(
    "/api/employees",
    response_model=list[Employee],
    summary="List all employees",
    tags=["employees"],
)
def get_employees() -> list[Employee]:
    """Return every employee as a JSON array.
    FastAPI converts the returned Python list into JSON.
    """
    return MOCK_EMPLOYEES


# is the server alive?
@app.get("/api/health", summary="Health check", tags=["system"])
def health_check() -> dict[str, str]:
    """Return a simple status message."""
    return {"status": "ok"}
