import json

import pytest

from config import TEST_JSON_PATH
from src.json_save import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def path():
    return TEST_JSON_PATH


@pytest.fixture
def vacancy():
    vacancy1 = Vacancy(
        "Python backend разработчик Middle+",
        120000,
        120000,
        "https://hh.ru/vacancy/92307003",
        "Поддерживать старый и разрабатывать новый функционал.",
    )
    vacancy2 = Vacancy(
        "Python разработчик (Django)", 60000, 100000, "https://hh.ru/vacancy/91636601", "Разработка проектов."
    )
    vacancies = [vacancy1, vacancy2]
    return vacancies


@pytest.fixture
def setup_data(tmp_path):
    test_data = [
        {"id": 1, "title": "Python Developer"},
        {"id": 2, "title": "Data Scientist"},
        {"id": 3, "title": "Web Developer"},
    ]
    file_path = tmp_path / "test_data.json"
    with open(file_path, "w", encoding="UTF-8") as file:
        json.dump(test_data, file, ensure_ascii=False, indent=4)
    yield file_path


def test_json_saver(path, vacancy):
    data = JSONSaver(path)
    data.write_data(vacancy)
    query = ["Django"]
    vac_json = data.get_data(query)
    with open(path, encoding="UTF-8") as file:
        hh = json.load(file)
        assert len(hh) == 2
        assert hh[0]["name"] == "Python backend разработчик Middle+"
        assert vac_json[0]["responsibility"] == "Разработка проектов."


def test_delete_data(setup_data):
    instance = JSONSaver(setup_data)
    instance.delete_data("Python")
    with open(setup_data, encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 2
        assert data[0]["title"] != "Python Developer"
