def test_create_employee(client):
    """
    Test that an employee can be created using the API.
    This test should fail initially because the endpoint
    is not implemented yet.
    """

    payload = {
        "full_name": "John Doe",
        "job_title": "Software Engineer",
        "country": "India",
        "salary": 100000
    }

    response = client.post("/employees", json=payload)

    # Expected successful creation
    assert response.status_code == 201

    data = response.json()

    assert data["full_name"] == payload["full_name"]
    assert data["job_title"] == payload["job_title"]
    assert data["country"] == payload["country"]
    assert data["salary"] == payload["salary"]
    assert "id" in data

def test_get_employee(client):
    """
    Test retrieving an employee by ID.
    This should fail initially because the endpoint
    GET /employees/{id} is not implemented yet.
    """

    create_payload = {
        "full_name": "Alice Smith",
        "job_title": "Data Engineer",
        "country": "India",
        "salary": 90000
    }

    create_response = client.post("/employees", json=create_payload)
    employee = create_response.json()

    employee_id = employee["id"]

    response = client.get(f"/employees/{employee_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == employee_id
    assert data["full_name"] == create_payload["full_name"]
    assert data["job_title"] == create_payload["job_title"]
    assert data["country"] == create_payload["country"]
    assert data["salary"] == create_payload["salary"]

def test_list_employees(client):
    """
    Test retrieving all employees.
    This test should fail initially because
    the GET /employees endpoint is not implemented.
    """

    employee1 = {
        "full_name": "Alice",
        "job_title": "Engineer",
        "country": "India",
        "salary": 80000
    }

    employee2 = {
        "full_name": "Bob",
        "job_title": "Manager",
        "country": "United States",
        "salary": 120000
    }

    client.post("/employees", json=employee1)
    client.post("/employees", json=employee2)

    response = client.get("/employees")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) >= 2

def test_delete_employee(client):
    """
    Test deleting an employee by ID.
    This test should fail initially because
    the DELETE /employees/{id} endpoint is not implemented yet.
    """

    payload = {
        "full_name": "Charlie Brown",
        "job_title": "Designer",
        "country": "India",
        "salary": 70000
    }

    create_response = client.post("/employees", json=payload)
    employee = create_response.json()
    employee_id = employee["id"]

    delete_response = client.delete(f"/employees/{employee_id}")

    assert delete_response.status_code == 200

    # Verify employee is deleted
    get_response = client.get(f"/employees/{employee_id}")

    assert get_response.status_code == 404

def test_update_employee(client):
    """
    Test updating an employee.
    This test should fail initially because
    PUT /employees/{id} endpoint is not implemented yet.
    """

    create_payload = {
        "full_name": "David Miller",
        "job_title": "Developer",
        "country": "India",
        "salary": 85000
    }

    create_response = client.post("/employees", json=create_payload)
    employee = create_response.json()
    employee_id = employee["id"]

    update_payload = {
        "full_name": "David Miller",
        "job_title": "Senior Developer",
        "country": "India",
        "salary": 95000
    }

    update_response = client.put(f"/employees/{employee_id}", json=update_payload)

    assert update_response.status_code == 200

    updated_employee = update_response.json()

    assert updated_employee["id"] == employee_id
    assert updated_employee["job_title"] == "Senior Developer"
    assert updated_employee["salary"] == 95000