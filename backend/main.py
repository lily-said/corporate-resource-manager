"""
Employee Resource Manager - FastAPI backend.

Running:
    uvicorn main:app --reload --port 8000

Opening:
    http://127.0.0.1:8000/api/employees   -> the JSON data
    http://127.0.0.1:8000/docs            -> interactive API documentation
    http://127.0.0.1:8000/openapi.json    -> the generated JSON schema
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from mock_data import MOCK_EMPLOYEES
from models import Employee

app = FastAPI(
    title="Employee Resource Manager API",
    description="A small API that serves employee records.",
    version="0.1.0",
)

ALLOWED_ORIGINS = [
    "http://localhost:4200",
    "http://127.0.0.1:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
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

@app.get(
    "/api/employees/{id}",
    response_model=Employee,
    summary="Get an employee by ID",
    tags=["employees"]
)
def get_employee_by_id(id: int) -> Employee:
    """Return an employee as a JSON array."""
    for employee in MOCK_EMPLOYEES:
        if employee.id == id:
            return employee
    raise HTTPException(status_code=404, detail=f"Employee with ID {id} not found")

# is the server alive?
@app.get(
    "/api/health",
    summary="Health check",
    tags=["system"]
)
def health_check() -> dict[str, str]:
    """Return a simple status message."""
    return {"status": "ok"}
