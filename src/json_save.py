import json
from abc import ABC, abstractmethod

from config import JSON_PATH
from src.vacancy import Vacancy


class AbstractSaver(ABC):
    """
    Абстрактный класс для JSON
    """

    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def get_data(self, data):
        pass


class JSONSaver(AbstractSaver):
    """
    Класс для работы с JSON файлами
    """

    def __init__(self):
        self.path = JSON_PATH

    def write_data(self, data: list | Vacancy) -> None:
        """
        Функция для записи данных в json-файл
        """
        json_vacancy = [item.__dict__ if type(data) is list else data.__dict__ for item in data]
        with open(self.path, "w", encoding="UTF-8") as file:
            json.dump(json_vacancy, file, ensure_ascii=False, indent=4)

    def get_data(self, query: list) -> list[dict]:
        """
        Функция для поиска в файле вакансий по запросу
        """
        get_query = []
        with open(self.path, encoding="UTF-8") as file:
            data = json.load(file)
        for item in data:
            for word in query:
                if word.lower() in str(item.values()).lower():
                    get_query.append(item)
                    break
        return get_query

    def delete_data(self, query: str) -> None:
        """
        Удаление вакансий из файла по ключевому слову
        """
        with open(self.path, encoding="UTF-8") as file:
            data = json.load(file)
            for item in data:
                for word in item.values():
                    if query.lower() in str(word).lower():
                        data.remove(item)
                        break
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
