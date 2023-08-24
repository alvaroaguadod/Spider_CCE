import json
import scrapy
from .spiders import CCESpider


class SpiderParameters:
    def __init__(self, spider: CCESpider):
        self.search = self.str_to_list(getattr(spider, "searchlist", None))
        self.category = self.str_to_list(getattr(spider, "category", None))
        self.from_date = getattr(spider, "from_date", None)
        self.to_date = getattr(spider, "to_date", None)

    #   depth

    #    def decode_str(self, s: str) -> str:
    #        if s:
    #            return json.loads(s)
    #        return s

    def str_to_list(self, text: str) -> list:
        if text:
            text = [
                x.strip().replace("[", "").replace("]", "") for x in text.split(",")
            ]
        return text
