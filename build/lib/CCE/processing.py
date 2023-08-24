import scrapy
import logging
import requests
from lxml import html


class ProcessingSearches:
    def __init__(self, parameters):
        self.parameters = parameters
        self.get_urls = []
        self.logger = logging.getLogger("CCESpider")
        self.total_pages = 0
        self.crawl()

    def crawl(self):
        new_list = []
        for search in self.parameters.search:
            # Check if there is more than one word
            if len(search.split()) > 1:
                # Replace spaces with a hyphen
                search = search.replace(" ", "+")
            url = f"https://cce.org.mx/?s={search}"
            response = requests.get(url)
            tree = html.fromstring(response.content)

            # Get the span element containing the total number of pages
            pages_span = tree.xpath(
                '//div[contains(@class, "wp-pagenavi")]//span[@class="pages"]'
            )[0]

            # Extract the last word of the span element, which contains the total number of pages
            total_pages = int(pages_span.text.split()[-1])
            print("Total number of pages:", total_pages)

            for depth in range(1, total_pages + 1):
                new_list.append(f"https://cce.org.mx/page/{depth}/?s={search}")

            self.get_urls = new_list
            self.search = ""


#        def category(self):
#            dict_categories = {
#                "oportunidades": "acceso-a-oportunidades",
#                "infraestructura" : "infraestructura",
#                "crecimiento e innovacion": "crecimiento-e-innovacion",
#                "transparencia" : "transparencia-justicia-y-legalidad",
#                "finanzas" : "finanzas-publicas",
#                "democracia" : "democracia-y-compromiso-social",
#                "relaciones internacionales" : "relaciones-internacionales",
#                "dimension social de las empresas" : "dimension-social-de-las-empresas",
#
#                "gobierno corporativo" : "gobierno-corporativo",
#                "publicaciones" : "publicaciones",
#                "alianzasestrategicas": "alianzas-estrategicas",
#                "publicaciones" : "publicaciones",
#                "documentos de analisis" : "documentos-de-analisis",
#                "documentos de interes" : "documentos-de-interes",
#                "comunicados" : "comunicados",
#                "prensa" : "prensa",
#                "trending" : "trending",
#
#                "francisco cervantes" : "francisco-cervantes",
#                "carlos salazar lomelin" : "carlos-salazar-lomelin",
#                "juan pablo castanon" : "juan-pablo-castanon",
#                "gerardo gutierrez candiani" : "gerardo-gutierrez-candiani",
#                "cce2030" : "cce2030",
#                "eventos" : "eventos",
#            }

# for category in self.parameters.category:
#    code = dict_categories.get(category.lower())
#    if code is not None:
#        url = f"https://cce.org.mx/category/{category}"
#        self.get_urls.append(url)
#    else:
#        self.logger.info(f'Error: la sección "{category}" no está disponible.')
