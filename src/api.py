from abc import ABC, abstractmethod
import requests

from config import HH_URL


class API(ABC):
    """
    Абстрактный класс для API
    """
    @abstractmethod
    def get_response(self):
        pass


class HeadHunterAPI(API):
    """
    Класс API HeadHunter
    """
    def __init__(self, query: str):
        self.query = query

    def get_response(self) -> list[dict]:
        """
        Функция для получения данных от API HeadHunter по заданным параметрам
        """
        params = {"text": self.query,
                  "page": 0,
                  "per_page": 100,
                  "search_field": "name",
                  "currency": "RUR",
                  "only_with_salary": True,
                  "area": 113}

        return requests.get(url=HH_URL, params=params).json()


if __name__ == '__main__':
    hh = HeadHunterAPI("Python")
    response = hh.get_response()
    print(response)
