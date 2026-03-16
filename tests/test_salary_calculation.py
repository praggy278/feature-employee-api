def test_salary_calculation_india(client):
    """
    Test salary calculation for an employee in India.
    India should have 10% TDS deduction.
    """

    payload = {
        "full_name": "Raj Sharma",
        "job_title": "Engineer",
        "country": "India",
        "salary": 100000
    }

    create_response = client.post("/employees", json=payload)
    employee = create_response.json()
    employee_id = employee["id"]

    response = client.get(f"/salary/{employee_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["employee_id"] == employee_id
    assert data["gross_salary"] == 100000
    assert data["tds"] == 10000
    assert data["net_salary"] == 90000


def test_salary_calculation_us(client):
    """
    Test salary calculation for an employee in United States.
    US should have 12% TDS deduction.
    """

    payload = {
        "full_name": "John Smith",
        "job_title": "Engineer",
        "country": "United States",
        "salary": 100000
    }

    create_response = client.post("/employees", json=payload)
    employee = create_response.json()

    response = client.get(f"/salary/{employee['id']}")

    assert response.status_code == 200

    data = response.json()

    assert data["tds"] == 12000
    assert data["net_salary"] == 88000


def test_salary_calculation_other_country(client):
    """
    Test salary calculation for other countries.
    No deductions should apply.
    """

    payload = {
        "full_name": "Pierre Dupont",
        "job_title": "Engineer",
        "country": "France",
        "salary": 100000
    }

    create_response = client.post("/employees", json=payload)
    employee = create_response.json()

    response = client.get(f"/salary/{employee['id']}")

    assert response.status_code == 200

    data = response.json()

    assert data["tds"] == 0
    assert data["net_salary"] == 100000