import json
from abc import ABC, abstractmethod

from config import JSON_PATH
from src.vacancy import Vacancy


class AbstractSaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancy_by_criteria(self, criteria):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(AbstractSaver):
    def __init__(self):
        self.filename = JSON_PATH
        self.vacancies = []

    def add_vacancy(self, vacancy):
        self.vacancies.append(vars(vacancy))
        # self.vacancies.extend(**vacancy)

    def get_vacancy_by_criteria(self, criteria):
        return [Vacancy(**vacancy) for vacancy in self.vacancies if
                all(vacancy.get(key) == value for key, value in criteria.items())]

    def delete_vacancy(self, vacancy):
        vacancy_data = vars(vacancy)
        if vacancy_data in self.vacancies:
            self.vacancies.remove(vacancy_data)
            self.save_to_file()
            return True
        return False

    def save_to_file(self):
        with open(self.filename, "w", encoding="UTF-8") as file:
            json.dump(self.vacancies, file, ensure_ascii=False, indent=4)
