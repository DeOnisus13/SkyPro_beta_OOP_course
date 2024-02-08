from src.api import HeadHunterAPI
from src.vacancy import Vacancy

hh = HeadHunterAPI("Python").get_response()
vacancies = [Vacancy(
    name=vacancy["name"],
    salary_from=vacancy["salary"]["from"],
    salary_to=vacancy["salary"]["to"],
    url=vacancy["alternate_url"],
    responsibility=vacancy["snippet"]["responsibility"]
) for vacancy in hh["items"]]


if __name__ == '__main__':
    print(vacancies[3].__str__())
