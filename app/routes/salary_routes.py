from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import crud
from ..services.salary_service import calculate_salary

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/salary/{employee_id}")
def get_salary(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id)

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    salary_data = calculate_salary(employee.salary, employee.country)

    return {
        "employee_id": employee.id,
        "gross_salary": salary_data["gross_salary"],
        "tds": salary_data["tds"],
        "net_salary": salary_data["net_salary"]
    }