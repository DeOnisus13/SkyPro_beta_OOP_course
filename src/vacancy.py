class Vacancy:
    def __init__(self, name: str, salary_from: int, salary_to: int, url: str, responsibility: str):
        self.name = name
        self.salary_from = self.validate_salary(salary_from)
        self.salary_to = self.validate_salary(salary_to)
        if self.salary_to < self.salary_from:
            self.salary_to = self.salary_from
        self.url = url
        self.responsibility = self.remove_highlight(responsibility)

    def __str__(self):
        return (f"{self.name}\n"
                f"Зарплата от {self.salary_from} до {self.salary_to}\n"
                f"URL - {self.url}\n"
                f"Обязанности: {self.responsibility}")

    @staticmethod
    def validate_salary(salary):
        if salary is None:
            return 0
        return salary

    @staticmethod
    def remove_highlight(responsibility):
        if isinstance(responsibility, str):
            responsibility = responsibility.replace("<highlighttext>", "")
            responsibility = responsibility.replace("</highlighttext>", "")
            return responsibility
        return ""
