"""
Data models for the API.

A "model" here is a Pydantic class: a normal Python class that also knows
how to validate its data and turn itself into JSON. FastAPI uses these
models to (a) check the data we send out and (b) auto-generate the API docs.
"""

from datetime import date
from pydantic import BaseModel, EmailStr, Field


class Employee(BaseModel):
    """A single employee record."""

    # `Field(...)` -> "this value is required"
    id: int = Field(
        ...,
        ge=1,  # >=1, no non-neg ids
        description="Unique identifier for the employee.",
        examples=[1],
    )
    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Full name of the employee.",
        examples=["Maimo Hasegawa"],
    )
    jobtitle: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Job title, e.g. 'Data Analyst'.",
        examples=["Sales Associate"],
    )
    department: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Department the employee belongs to.",
        examples=["Finance"],
    )
    # `EmailStr` rejects anything that is not a valid email address.
    email: EmailStr = Field(
        ...,
        description="Work email address.",
        examples=["maimo.hasegawa@example.com"],
    )
    phone: str = Field(
        ...,
        min_length=1,
        max_length=30,
        description="Contact phone number.",
        examples=["555-1234"],
    )
    joindate: date = Field(
        ...,
        description="The day the employee joined the company (YYYY-MM-DD).",
        examples=["1990-05-15"],
    )
    imgUrl: str = Field(
        ...,
        description="URL of the employee's profile picture.",
        examples=["https://picsum.photos/seed/1/400/400"],
    )

    # `model_config` -> optional settings for the model.
    # adding an example employee for readability.
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "name": "Maimo Hasegawa",
                "jobtitle": "Sales Associate",
                "department": "Finance",
                "email": "maimo.hasegawa@example.com",
                "phone": "555-1234",
                "joindate": "1990-05-15",
                "imgUrl": "https://picsum.photos/seed/1/400/400",
            }
        }
    }
