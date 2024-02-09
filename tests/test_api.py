from src.api import HeadHunterAPI


def test_get_response():
    api_hh = HeadHunterAPI("python").get_response()
    assert len(api_hh) == 10
