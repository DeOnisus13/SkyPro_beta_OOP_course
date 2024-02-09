from config import JSON_PATH
from src.api import HeadHunterAPI
from src.json_save import JSONSaver
from src.vacancy import Vacancy


def main():
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    data = HeadHunterAPI(search_query).get_response()
    vacancies = Vacancy.init_hh(data)
    vacancies = list(sorted(vacancies, reverse=True))

    json_save = JSONSaver(JSON_PATH)
    json_save.write_data(vacancies)

    request_response = json_save.get_data(filter_words)
    user_response = Vacancy.init_json(request_response)
    if len(user_response) >= 5:
        for value in range(top_n):
            print(user_response[value])
    else:
        for value in range(len(user_response)):
            print(user_response[value])


if __name__ == "__main__":
    main()
