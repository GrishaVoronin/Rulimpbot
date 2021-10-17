import requests
from bs4 import BeautifulSoup as BS, ResultSet

from core.olymp import OlympItem
from core.olymps_parser import urls


class OlympsParser:
    number_of_olymps: int

    def __init__(self, number_of_olymps: int):
        self.number_of_olymps = number_of_olymps

    def get_olymps_by_request(self, request: str) -> list[OlympItem]:
        bs = _get_html_page(urls.get_request_url(request))
        return OlympsParser._get_olymps_items(self, bs)

    def get_olymps_by_subject(self, subject_id: str):
        bs = _get_html_page(urls.get_by_subject_url(subject_id))
        return OlympsParser._get_olymps_items(self, bs)

    @staticmethod
    def _get_olymps_items(self, bs: BS) -> list[OlympItem]:
        titles_content = _get_item_content(bs_obj=bs, html_tag="span", class_="headline")
        dates_content = _get_item_content(bs_obj=bs, html_tag="span", class_="red")
        links_content = _get_item_content(bs_obj=bs, html_tag="a", class_="none_a black")
        forms_content = _get_item_content(bs_obj=bs, html_tag="span", class_="classes_dop")
        ratings_content = _get_item_content(bs_obj=bs, html_tag="span", class_="pl_rating")
        abouts_content = _get_item_content(bs_obj=bs, html_tag="a", class_="none_a black olimp_desc")

        abouts = [i.get_text() for i in abouts_content]
        ratings = [i.get_text() for i in ratings_content]
        forms = [i.get_text() for i in forms_content]
        dates = [i.get_text() for i in dates_content]
        titles = []
        links = []

        for i in range(len(titles_content)):
            if i % 2 == 0:  # Сайт гипер-кривой, поэтому это -- самое нормальное решение
                titles.append(titles_content[i].get_text())

        for i in links_content:
            link = i['href']
            if link not in links:
                links.append(link)

        found_olymps = []

        for i in range(OlympsParser._get_olymps_count(self, titles)):
            try:
                found_olymps.append(
                    OlympItem(
                        olymp_title=titles[i],
                        link=f"{urls.BASE_URL}{links[i][1:]}",
                        about_info=abouts[i],
                        forms_participates=forms[i],
                        date_info=dates[i],
                        rating=float(ratings[i].replace(',', '.'))
                    )
                )
            except IndexError:
                pass
        return found_olymps

    @staticmethod
    def _get_olymps_count(self, titles):
        return len(titles) if len(titles) < self.number_of_olymps else self.number_of_olymps


def _get_html_page(url: str) -> BS:
    page = requests.get(url)
    return BS(page.text, 'html.parser')


def _get_item_content(bs_obj: BS, html_tag: str, class_: str) -> ResultSet:
    return bs_obj.find_all(html_tag, class_=class_)
