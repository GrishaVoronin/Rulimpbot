from dataclasses import dataclass


@dataclass
class OlympItem:
    """Имплементирует олимпиаду из общего списка с небольшим описанием и главной информацией"""
    link: str
    olymp_title: str
    about_info: str
    forms_participates: str
    date_info: str
    rating: float

    def __init__(self, link: str, olymp_title: str, about_info: str, forms_participates: str, date_info: str,
                 rating: float):
        self.link = link
        self.olymp_title = olymp_title
        self.about_info = about_info
        self.forms_participates = forms_participates
        self.date_info = date_info
        self.rating = rating


class FullOlympItem:
    """Имлементирует все данные об олимпиаде (при полном открытии)"""
    olymp_item: OlympItem
    updates: list[str]
    features: list[str]
    preparation: list[dict]

    def __init__(self, olymp_item: OlympItem, updates: list[str], features: list[str], preparation: list[dict]):
        self.olymp_item = olymp_item
        self.updates = updates
        self.features = features
        self.preparation = preparation
