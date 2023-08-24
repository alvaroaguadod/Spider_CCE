import scrapy
import logging
from datetime import datetime
import pandas as pd
from typing import List
import requests
from lxml import html


class ProcessingSearches:
    def __init__(self, parameters):
        self.parameters = parameters
        self.get_urls = []
        self.logger = logging.getLogger("CCESpider")
        self.total_pages = 0
        self.category()
        self.date()
        self.crawl()

    def crawl(self, searchlist=None):
        # If searchlist is None, set it to an empty list
        searchlist = self.parameters.search
        if searchlist is None:
            return
        new_list = []

        for searchlist in self.parameters.search:
            # Check if there is more than one word
            if len(searchlist.split()) > 1:
                # Replace spaces with a hyphen
                searchlist = searchlist.replace(" ", "+")
            url = f"https://cce.org.mx/?s={searchlist}"
            response = requests.get(url)
            tree = html.fromstring(response.content)
            # Check if the category page contains the desired xpath
            if tree.xpath('//div[contains(@class, "wp-pagenavi")]//span[@class="pages"]'):
                pages_span = tree.xpath(
                    '//div[contains(@class, "wp-pagenavi")]//span[@class="pages"]'
                )[0]
                # Extract the last word of the span element, which contains the total number of pages
                total_pages = int(pages_span.text.split()[-1])
                print("Total number of pages:", total_pages)

                # Create a list of urls for all pages of the category
                for depth in range(1, total_pages + 1):
                    new_list.append(f"https://cce.org.mx/page/{depth}/?s={searchlist}")

                self.get_urls = new_list
                self.search = ""
            else:
                self.logger.info(f"Error: The section {searchlist} does not contain the desired XPath.")
                self.get_urls.append(url)


    def category(self):
        new_list = []
        list_available_categories = (
            "acceso a oportunidades", # "acceso-a-oportunidades",
            "infraestructura", #"infraestructura",
            "crecimiento e innovacion", #"crecimiento-e-innovacion",
            "transparencia justicia y legalidad", #"transparencia-justicia-y-legalidad",
            "finanzas publicas", #"finanzas-publicas"
            "democracia y compromiso social", #"democracia-y-compromiso-social"
            "relaciones internacionales", #"relaciones-internacionales"
            "dimension social de las empresas", #"dimension-social-de-las-empresas"

            "gobierno corporativo", # "gobierno-corporativo",
            "publicaciones", # "publicaciones",
            "alianzas estrategicas", # "alianzas-estrategicas",
            "documentos de analisis", # "documentos-de-analisis",
            "documentos de interes", # "documentos-de-interes",
            "comunicados", # "comunicados",
            "prensa", # "prensa",
            "trending", # "trending",

            "francisco cervantes", # "francisco-cervantes",
            "carlos salazar lomelin", # "carlos-salazar-lomelin",
            "juan pablo castanon", # "juan-pablo-castanon",
            "gerardo gutierrez candiani", # "gerardo-gutierrez-candiani",
            "cce2030", # "cce2030",
            "eventos", # "eventos",
        )

        if self.parameters.category is not None:
            for c in self.parameters.category:
                if c in list_available_categories:
                    c = c.replace(" ", "-")
                    c.lower()
                    url = f"https://cce.org.mx/category/{c}/"
                    print(url)
                    response = requests.get(url)
                    tree = html.fromstring(response.content)


                    # Check if the category page contains the desired xpath
                    if tree.xpath('//div[contains(@class, "wp-pagenavi")]//span[@class="pages"]'):
                        pages_span = tree.xpath(
                            '//div[contains(@class, "wp-pagenavi")]//span[@class="pages"]'
                        )[0]

                        # Extract the last word of the span element, which contains the total number of pages
                        total_pages = int(pages_span.text.split()[-1])
                        print("Total number of pages:", total_pages)

                        # Create a list of urls for all pages of the category
                        for depth in range(1, total_pages + 1):
                            new_list.append(f"https://cce.org.mx/category/{c}/page/{depth}")

                        self.get_urls = new_list
                        self.search = ""

                    else:
                        self.logger.info(f"Error: The section {c} does not contain the desired XPath.")
                        self.get_urls.append(url)

                else:
                    self.logger.info(f"Error: The section {c} does not exist.")
            

    def get_date(self) -> str:
           if self.from_date and self.to_date:
               dates = self.range_dates(self.from_date, self.to_date)
               if dates:
                   return dates
           elif self.from_date:
               return f"[{self.from_date}]"
           elif self.to_date:
               return f"[{self.to_date}]"
           return None

    def range_dates(self, start="2023-01-01", end=None) -> List[str]:
        if end is None:
            end = datetime.strftime(datetime.utcnow(), "%Y-%m-%d")
        to_datetime = lambda x: datetime.strptime(x, "%Y-%m-%d")
        start, end = to_datetime(start), to_datetime(end)
        dates = list(
            map(
                lambda x: x.strftime("%Y/%m/%d"),  # change the item "-" to "/".
                pd.period_range(start, end, freq="D").tolist()[:-1] + [end],
            )
        )
        return dates

    def date(self):
        if (
            self.parameters.from_date is not None
            and self.parameters.to_date is not None
        ):
            dates = self.range_dates(self.parameters.from_date, self.parameters.to_date)
            if dates:
                for date in dates:
                    url = f"https://cce.org.mx/{date}/"
                    self.get_urls.append(url)
        elif self.parameters.from_date is not None:
            dates = self.range_dates(self.parameters.from_date)
            if dates:
                for date in dates:
                    url = f"https://cce.org.mx/{date}/"
                    self.get_urls.append(url)
        elif self.parameters.to_date is not None:
            dates = self.range_dates(end=self.parameters.to_date)
            if dates:
                for date in dates:
                    url = f"https://cce.org.mx/{date}/"
                    self.get_urls.append(url)
