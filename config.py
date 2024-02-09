from pathlib import Path

HH_URL = "https://api.hh.ru/vacancies"

ROOT_PATH = Path(__file__).parent
JSON_PATH = ROOT_PATH.joinpath("data", "vacancies.json")
TEST_JSON_PATH = ROOT_PATH.joinpath("tests", "test_json.json")
