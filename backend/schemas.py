from pydantic import BaseModel
from typing import Optional, List
from datetime import date


# ---------------------
# AUTH SCHEMAS
# ---------------------

class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


# ---------------------
# EMPLOYEE SCHEMAS
# ---------------------

class EmployeeCreate(BaseModel):
    name: str
    email: str
    role: str
    status: str


class Employee(BaseModel):
    id: int
    name: str
    email: str
    role: str
    status: str

    class Config:
        from_attributes = True


# ---------------------
# TASK SCHEMAS
# ---------------------

class TaskCreate(BaseModel):
    title: str
    description: str
    status: str
    due_date: date
    employee_id: int


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str
    due_date: date
    employee_id: int

    class Config:
        from_attributes = True
