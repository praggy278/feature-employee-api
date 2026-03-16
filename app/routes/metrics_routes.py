from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..import schemas
from ..services.metrics_service import (
    get_country_salary_metrics,
    get_job_salary_metrics
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/metrics/country/{country}", response_model=schemas.CountrySalaryMetrics)
def country_metrics(country: str, db: Session = Depends(get_db)):
    metrics = get_country_salary_metrics(db, country)

    if not metrics:
        raise HTTPException(status_code=404, detail="No employees found for this country")

    return metrics


@router.get("/metrics/job/{job_title}", response_model=schemas.JobSalaryMetrics)
def job_metrics(job_title: str, db: Session = Depends(get_db)):
    metrics = get_job_salary_metrics(db, job_title)

    if not metrics:
        raise HTTPException(status_code=404, detail="No employees found for this job title")

    return metrics