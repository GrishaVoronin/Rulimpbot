BASE_URL = "https://olimpiada.ru/"


def get_request_url(request: str) -> str:
    return f'{BASE_URL}search?q={request}'


def get_math_olymps_url() -> str:
    return f'{BASE_URL}activities?type=any&subject%5B6%5D=on&class=any&period_date=&period=year'


def get_comp_science_olymps_url() -> str:
    return f'{BASE_URL}activities?type=any&subject%5B7%5D=on&class=any&period_date=&period=year'
