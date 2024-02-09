from src.api import HeadHunterAPI
from src.vacancy import Vacancy


def main():
    hh = HeadHunterAPI("Python").get_response()
    vacancies = [Vacancy(
        name=vacancy["name"],
        salary_from=vacancy["salary"]["from"],
        salary_to=vacancy["salary"]["to"],
        url=vacancy["alternate_url"],
        responsibility=vacancy["snippet"]["responsibility"]
    ) for vacancy in hh["items"]]
    return vacancies


if __name__ == '__main__':

    for x in main():
        print(x)
        print("-"*40)
