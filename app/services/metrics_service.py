from sqlalchemy.orm import Session
from sqlalchemy import func
from ..models import Employee


def get_country_salary_metrics(db: Session, country: str):
    result = db.query(
        func.min(Employee.salary),
        func.max(Employee.salary),
        func.avg(Employee.salary)
    ).filter(Employee.country == country).first()

    if not result or result[0] is None:
        return None

    return {
        "country": country,
        "min_salary": result[0],
        "max_salary": result[1],
        "average_salary": int(result[2])
    }


def get_job_salary_metrics(db: Session, job_title: str):
    result = db.query(
        func.avg(Employee.salary)
    ).filter(Employee.job_title == job_title).first()

    if not result or result[0] is None:
        return None

    return {
        "job_title": job_title,
        "average_salary": int(result[0])
    }