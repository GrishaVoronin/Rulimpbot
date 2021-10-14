BASE_URL = "https://olimpiada.ru/"


def get_request_url(request: str) -> str:
    return f'{BASE_URL}search?q={request}'


def get_by_subject_url(subject_id: str) -> str:
    return f'{BASE_URL}activities?type=any&subject%5B{subject_id}%5D=on&class=any&period_date=&period=week'
