"""

"""


class Media:
    def __init__(self, title: str, subtitle: str, photo_url: str):
        self.__title = title
        self.__subtitle = subtitle
        self.__photo_url = photo_url

    def title(self) -> str:
        return self.__title

    def subtitle(self) -> str:
        return self.__subtitle

    def photo_url(self) -> str:
        return self.__photo_url
