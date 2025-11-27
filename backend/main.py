from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import Base, engine, get_db
from backend import models, schemas
from backend.auth import router as auth_router, get_current_user

from fastapi.middleware.cors import CORSMiddleware



# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # You can restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)


@app.get("/")
def read_root():
    return {"message": "Employee Task Management API is running"}


# ------------------------------------------------------------
# EMPLOYEE ENDPOINTS (PROTECTED)
# ------------------------------------------------------------

@app.post("/employees", response_model=schemas.Employee)
def create_employee(
    emp_in: schemas.EmployeeCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    existing = db.query(models.Employee).filter(models.Employee.email == emp_in.email).first()
    if existing:
        raise HTTPException(400, "Email already exists")

    emp = models.Employee(
        name=emp_in.name,
        email=emp_in.email,
        role=emp_in.role,
        status=emp_in.status,
    )

    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp


@app.get("/employees", response_model=List[schemas.Employee])
def list_employees(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return db.query(models.Employee).all()


@app.get("/employees/{employee_id}", response_model=schemas.Employee)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    emp = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not emp:
        raise HTTPException(404, "Employee not found")
    return emp


@app.put("/employees/{employee_id}", response_model=schemas.Employee)
def update_employee(
    employee_id: int,
    emp_update: schemas.EmployeeCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    emp = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not emp:
        raise HTTPException(404, "Employee not found")

    emp.name = emp_update.name
    emp.email = emp_update.email
    emp.role = emp_update.role
    emp.status = emp_update.status

    db.commit()
    db.refresh(emp)
    return emp


@app.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    emp = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not emp:
        raise HTTPException(404, "Employee not found")

    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted successfully"}


# ------------------------------------------------------------
# TASK ENDPOINTS (PROTECTED)
# ------------------------------------------------------------

@app.post("/tasks", response_model=schemas.Task)
def create_task(
    task_in: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    task = models.Task(
        title=task_in.title,
        description=task_in.description,
        status=task_in.status,
        due_date=task_in.due_date,
        employee_id=task_in.employee_id
    )

    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@app.get("/tasks", response_model=List[schemas.Task])
def list_tasks(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return db.query(models.Task).all()


@app.get("/tasks/{task_id}", response_model=schemas.Task)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(404, "Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(
    task_id: int,
    task_update: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(404, "Task not found")

    task.title = task_update.title
    task.description = task_update.description
    task.status = task_update.status
    task.due_date = task_update.due_date
    task.employee_id = task_update.employee_id

    db.commit()
    db.refresh(task)
    return task


@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(404, "Task not found")

    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}


# ------------------------------------------------------------
# RELATIONSHIP ROUTES (PROTECTED)
# ------------------------------------------------------------

@app.get("/employees/{employee_id}/tasks", response_model=List[schemas.Task])
def get_tasks_for_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    emp = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not emp:
        raise HTTPException(404, "Employee not found")
    return emp.tasks


@app.get("/tasks/{task_id}/employee", response_model=schemas.Employee)
def get_employee_of_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task or not task.employee:
        raise HTTPException(404, "No employee assigned to this task")
    return task.employee


@app.get("/tasks/{task_id}/employee/name")
def get_employee_name_from_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task or not task.employee:
        raise HTTPException(404, "No employee assigned to this task")
    return {"employee_name": task.employee.name}


@app.get("/employees/{employee_id}/task-titles")
def get_task_titles_for_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    emp = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not emp:
        raise HTTPException(404, "Employee not found")

    titles = [task.title for task in emp.tasks]
    return {"task_titles": titles}
