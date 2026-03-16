# Employee Salary API

A RESTful API for managing employees and calculating salary deductions
based on country-specific tax rules.

The API supports: - Employee CRUD operations - Salary deduction
calculation - Salary analytics and metrics

This project was implemented using Test-Driven Development (TDD).

------------------------------------------------------------------------

## Tech Stack

-   Python 3.10+
-   FastAPI
-   SQLite
-   SQLAlchemy
-   Pytest

------------------------------------------------------------------------

## Project Structure
```text
employee-api/ 
├── app/ 
│ ├── routes/ 
│ │ ├── employee_routes.py 
│ │ ├── salary_routes.py 
│ │ └── metrics_routes.py 
│ ├── services/ 
│ │ ├── salary_service.py 
│ │ └── metrics_service.py 
│ ├── crud.py 
│ ├── models.py 
│ ├── schemas.py 
│ ├── database.py 
│ └── main.py 
├── tests/
│ ├── test_employee_crud.py 
│ ├── test_salary_calculation.py 
│ └── test_salary_metrics.py 
├── requirements.txt 
└── README.md
```
------------------------------------------------------------------------

## Setup Instructions

1.  Clone the repository git clone cd employee-api

2.  Create virtual environment python -m venv venv

Activate: Mac/Linux: source venv/bin/activate Windows: venv

3.  Install dependencies pip install -r requirements.txt

4.  Run the API uvicorn app.main:app –reload

Server: http://127.0.0.1:8000

Swagger Docs: http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## Running Tests

Run: pytest

Expected: 10 passed

------------------------------------------------------------------------

## API Endpoints

Create Employee POST /employees

Get Employee GET /employees/{employee_id}

List Employees GET /employees

Update Employee PUT /employees/{employee_id}

Delete Employee DELETE /employees/{employee_id}

------------------------------------------------------------------------

### Salary Calculation

GET /salary/{employee_id}

Deduction Rules: India → 10% United States → 12% Other countries → 0%

Example Response: { “employee_id”: 1, “gross_salary”: 100000, “tds”:
10000, “net_salary”: 90000 }

------------------------------------------------------------------------

### Salary Metrics

Country Metrics GET /metrics/country/{country}

Returns: - minimum salary - maximum salary - average salary

Job Metrics GET /metrics/job/{job_title}

Returns: - average salary

------------------------------------------------------------------------

## Architecture

Routes → Services → CRUD → Database

Routes: HTTP handling Services: business logic CRUD: database operations
Models: ORM models Schemas: request/response validation

------------------------------------------------------------------------

## Test-Driven Development

Development followed: Red → Green → Refactor

1.  Write failing test
2.  Implement minimal code
3.  Refactor

Commit history reflects this workflow.

------------------------------------------------------------------------

## AI Usage

AI tools were used to: - scaffold project structure - generate test case
ideas - draft documentation - review architecture decisions

All generated code was reviewed and validated manually.

AI tool used: ChatGPT

------------------------------------------------------------------------

## Future Improvements

-   pagination for employee listing
-   authentication/authorization
-   Docker containerization
-   CI/CD pipeline
-   database migrations (Alembic)

------------------------------------------------------------------------

#### Author: praggy278
