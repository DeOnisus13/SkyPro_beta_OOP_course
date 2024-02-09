import json
from abc import ABC, abstractmethod

from config import JSON_PATH
from src.vacancy import Vacancy


class AbstractSaver(ABC):
    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def get_data(self, data):
        pass


class JSONSaver(AbstractSaver):
    def __init__(self):
        self.path = JSON_PATH

    def read_data(self) -> list[dict]:
        with open(self.path, encoding="UTF-8") as file:
            return json.load(file)

    def write_data(self, data: list | Vacancy):
        json_vacancy = [item.__dict__ if type(data) is list else data.__dict__ for item in data]
        with open(self.path, "w", encoding="UTF-8") as file:
            json.dump(json_vacancy, file, ensure_ascii=False, indent=4)

    def get_data(self, query: list) -> list[dict]:
        get_query = []
        with open(self.path, encoding="UTF-8") as file:
            data = json.load(file)
        for item in data:
            for word in query:
                if word.lower() in str(item.values()).lower():
                    get_query.append(item)
                    break
        return get_query
