from sqlalchemy.orm import Session
from . import models, schemas


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def get_employees(db: Session):
    return db.query(models.Employee).all()


def delete_employee(db: Session, employee_id: int):
    employee = get_employee(db, employee_id)

    if employee:
        db.delete(employee)
        db.commit()

    return employee


def update_employee(db: Session, employee_id: int, updated_data: schemas.EmployeeCreate):
    employee = get_employee(db, employee_id)

    if not employee:
        return None

    employee.full_name = updated_data.full_name
    employee.job_title = updated_data.job_title
    employee.country = updated_data.country
    employee.salary = updated_data.salary

    db.commit()
    db.refresh(employee)

    return employee