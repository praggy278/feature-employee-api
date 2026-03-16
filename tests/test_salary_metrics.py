def test_country_salary_metrics(client):
    """
    Test salary metrics for a specific country.
    Should return min, max, and average salary.
    """

    employees = [
        {
            "full_name": "Alice",
            "job_title": "Engineer",
            "country": "India",
            "salary": 50000
        },
        {
            "full_name": "Bob",
            "job_title": "Engineer",
            "country": "India",
            "salary": 100000
        },
        {
            "full_name": "Charlie",
            "job_title": "Manager",
            "country": "India",
            "salary": 150000
        }
    ]

    for emp in employees:
        client.post("/employees", json=emp)

    response = client.get("/metrics/country/India")

    assert response.status_code == 200

    data = response.json()

    assert data["country"] == "India"
    assert data["min_salary"] == 50000
    assert data["max_salary"] == 150000
    assert data["average_salary"] == 100000


def test_job_title_average_salary(client):
    """
    Test average salary for a given job title.
    """

    employees = [
        {
            "full_name": "David",
            "job_title": "Developer",
            "country": "India",
            "salary": 80000
        },
        {
            "full_name": "Emma",
            "job_title": "Developer",
            "country": "United States",
            "salary": 120000
        }
    ]

    for emp in employees:
        client.post("/employees", json=emp)

    response = client.get("/metrics/job/Developer")

    assert response.status_code == 200

    data = response.json()

    assert data["job_title"] == "Developer"
    assert data["average_salary"] == 100000