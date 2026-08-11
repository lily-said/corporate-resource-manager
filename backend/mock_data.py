"""
Temporary in-memory data.

Keeping fake data in its own file means that swapping 
in a real database causes a change to `main.py` only.
"""

from models import Employee

MOCK_EMPLOYEES: list[Employee] = [
    Employee(id=1, name="Maimo Hasegawa", role="Sales Associate", department="Finance"),
    Employee(id=2, name="Fuze Kramer", role="Marketing Manager", department="Marketing"),
    Employee(id=3, name="Jose L. Meina", role="Project Manager", department="Operations"),
    Employee(id=4, name="Kornelia Maciejewska", role="Data Analyst", department="Analytics"),
    Employee(id=5, name="Ebelegbulam Amechi", role="Financial Analyst", department="Finance"),
]
