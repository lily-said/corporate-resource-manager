"""
Data models for the API.

A "model" here is a Pydantic class: a normal Python class that also knows
how to validate its data and turn itself into JSON. FastAPI uses these
models to (a) check the data we send out and (b) auto-generate the API docs.
"""

from pydantic import BaseModel, Field


class Employee(BaseModel):
    """A single employee record.
    """

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
    role: str = Field(
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

    # `model_config` -> optional settings for the model.
    # adding an example employee for readability.
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "name": "Maimo Hasegawa",
                "role": "Sales Associate",
                "department": "Finance",
            }
        }
    }
