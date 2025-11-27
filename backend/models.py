from datetime import datetime, date

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, Text , Boolean
from sqlalchemy.orm import relationship

from backend.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, nullable=False)
    status = Column(String, default="ACTIVE")
    created_at = Column(DateTime, default=datetime.utcnow)

    tasks = relationship("Task", back_populates="employee", cascade="all, delete")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String, default="TODO")
    due_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=True)
    employee = relationship("Employee", back_populates="tasks")



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
