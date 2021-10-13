import requests
from core.olymps_parser import urls
from bs4 import BeautifulSoup as BS, ResultSet
from core.olymp import OlympItem


class OlympsParser:
    number_of_olymps: int

    def __init__(self, number_of_olymps: int):
        self.number_of_olymps = number_of_olymps

    def get_olymps_by_request(self, request: str) -> list[OlympItem]:
        found_olymps = []

        bs = _get_html_page(request)
        olymps_titles_content = _get_headlines(bs)
        dates_info_content = _get_dates_info_content(bs)
        links_content = _get_links(bs)
        forms_content = _get_forms(bs)
        rating_content = _get_ration(bs)
        about_info_content = _get_about_info(bs)

        about_infos = [i.get_text() for i in about_info_content]

        ratings = [i.get_text() for i in rating_content]

        forms = [i.get_text() for i in forms_content]

        olymps_titles = []

        for i in range(len(olymps_titles_content)):
            if i % 2 == 0:  # Сайт гипер-кривой, поэтому это -- самое нормальное решение
                olymps_titles.append(olymps_titles_content[i].get_text())

        olymps_dates_info = [i.get_text() for i in dates_info_content]
        links = []

        for i in links_content:
            link = i['href']
            if link not in links:
                links.append(link)

        if len(olymps_titles) < self.number_of_olymps:
            counter = len(olymps_titles)
        else:
            counter = self.number_of_olymps

        for i in range(counter):
            found_olymps.append(
                OlympItem(
                    olymp_title=olymps_titles[i],
                    link=links[i],
                    about_info=about_infos[i],
                    forms_participates=forms[i],
                    date_info=olymps_dates_info[i],
                    rating=float(ratings[i].replace(',', '.'))
                )
            )

        return found_olymps


def _get_html_page(request: str) -> BS:
    page = requests.get(urls.get_request_url(request))
    return BS(page.text, 'html.parser')


def _get_headlines(bs: BS) -> ResultSet:
    content = bs.find_all("span", class_="headline")
    return content


def _get_dates_info_content(bs: BS) -> ResultSet:
    content = bs.find_all("span", class_="red")
    return content


def _get_links(bs: BS) -> ResultSet:
    content = bs.find_all("a", class_="none_a black")
    return content


def _get_forms(bs: BS) -> ResultSet:
    content = bs.find_all("span", class_="classes_dop")
    return content


def _get_ration(bs: BS) -> ResultSet:
    content = bs.find_all("span", class_="pl_rating")
    return content


def _get_about_info(bs: BS) -> ResultSet:
    content = bs.find_all("a", class_="none_a black olimp_desc")
    return content
