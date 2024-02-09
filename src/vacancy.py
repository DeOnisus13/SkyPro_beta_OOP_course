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
                f"Обязанности: {self.responsibility}\n"
                f"------------------------------------")

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

    @classmethod
    def init_hh(cls, data: list) -> list:
        vacancy_list = [cls(
            name=vacancy["name"],
            salary_from=vacancy["salary"]["from"],
            salary_to=vacancy["salary"]["to"],
            url=vacancy["alternate_url"],
            responsibility=vacancy["snippet"]["responsibility"]
        ) for vacancy in data["items"]]
        return vacancy_list

    @classmethod
    def init_json(cls, data: list) -> list:
        return [cls(**item) for item in data]

    def __gt__(self, other):
        return self.salary_to > other.salary_to

    def __lt__(self, other):
        return self.salary_to < other.salary_to
