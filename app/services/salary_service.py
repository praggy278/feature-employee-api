def calculate_salary(gross_salary: float, country: str):
    country = country.lower()

    if country == "india":
        tds = gross_salary * 0.10
    elif country == "united states":
        tds = gross_salary * 0.12
    else:
        tds = 0

    net_salary = gross_salary - tds

    return {
        "gross_salary": gross_salary,
        "tds": tds,
        "net_salary": net_salary
    }