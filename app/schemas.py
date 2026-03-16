from pydantic import BaseModel
from pydantic import Field


class EmployeeCreate(BaseModel):
    full_name: str
    job_title: str
    country: str
    salary: float = Field(gt=0)


class Employee(EmployeeCreate):
    id: int

    class Config:
        orm_mode = True

class SalaryCalculation(BaseModel):
    employee_id: int
    gross_salary: float
    tds: float
    net_salary: float


class CountrySalaryMetrics(BaseModel):
    country: str
    min_salary: float
    max_salary: float
    average_salary: float


class JobSalaryMetrics(BaseModel):
    job_title: str
    average_salary: float