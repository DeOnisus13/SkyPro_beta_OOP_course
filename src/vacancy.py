class Vacancy:
    def __init__(self, name: str, salary_from: int, salary_to: int, url: str, responsibility: str):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = url
        self.responsibility = responsibility

    def __str__(self):
        return (f"{self.name}"
                f"Зарплата от {self.salary_from} до {self.salary_to}"
                f"URL - {self.url}"
                f"Обязанности: {self.responsibility}")
