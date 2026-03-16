from fastapi import FastAPI
from .database import engine
from . import models
from .routes import employee_routes, salary_routes, metrics_routes

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Salary API",
    version="1.0.0"
)

app.include_router(employee_routes.router, tags=["Employees"])
app.include_router(salary_routes.router, tags=["Salary"])
app.include_router(metrics_routes.router, tags=["Metrics"])


@app.get("/")
def health_check():
    return {"status": "ok"}