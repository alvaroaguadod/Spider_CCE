import scrapy
from scrapy.loader import ItemLoader
from scrapy import Item
from scrapy.spiders import CrawlSpider, Rule
from CCE.items import CCEItem
from CCE.parameters import SpiderParameters
from CCE.processing import ProcessingSearches


class CCESpiderSpider(scrapy.Spider):
    name = "CCESpider"
    download_delay = 1
    urls_list = []

    def start_requests(self):
        parameters = SpiderParameters(self)
        urls_list = ProcessingSearches(parameters).get_urls
        for link in urls_list:
            # print("Scraping page: " + link)
            yield scrapy.Request(url=link, callback=self.parse)

    def parse(self, response):
        # Create a new list for all the articles in the pages
        articles_list = response.xpath(
            '//div[contains(@class, "col-md-8")]//article[contains(@id, "post-")]/div/div/h3/a/@href'
        ).getall()
        # print(articles_list)
        for article in articles_list:
            # print("ARTICLE: " + article)
            yield scrapy.Request(url=article, callback=self.parse_item)

    def parse_item(self, response):
        item = ItemLoader(CCEItem(), response)
        item.add_xpath(
            "title",
            '//div[contains(@class, "blog-post-single")]//div[contains(@class, "post-details")]/h1[contains(@class, "post-title")]/text()',
        )
        item.add_xpath(
            "author",
            '//div[contains(@class, "blog-post-single")]//div[contains(@class, "post-author")]//span[@class="fn"]//text()',
        )
        item.add_xpath(
            "date",
            '//div[contains(@class, "blog-post-single")]//div[contains(@class, "post-date")]/time[contains(@class, "entry-date published updated")]/text()',
        )
        item.add_xpath(
            "text",
            '//div[contains(@class, "blog-post-single")]//div[contains(@class, "entry-content")]/p//text()',
        )
        yield item.load_item()


# OTRAS FUNCIONES
#
#    def parse_blog(self, response):
#        items_list= response.xpath('/html/body/div[2]/div[2]/div/div/div/article/div/div/div/div/div/div/div/div/div/a').extract() + response.xpath('/html/body/div[2]/div[2]/div/div/div/article/div/div[1]/div/div/div[3]/div/div/div[2]/h3/a').extract()
#        for link in items_list:
#            yield scrapy.Request(url= link, callback=self.parseItemBlog)


# Links recogidos CCE -> https://cce.org.mx/blog/
# class="ultp-block-content-wrap ultp-first-postlist-2" #articulos
# /html/body/div[2]/div[2]/div/div/div/article/div/div/div/div/div/div/div/div/div/a #leermas o masinformacion
# /html/body/div[2]/div[2]/div/div/div/article/div/div[1]/div/div/div[3]/div/div/div[2]/h3/a #title
# /html/body/div[2]/div[2]/div/div/div/article/div/div[2]/div/div/div/div/div/div/span/a #title Lo más popular
# /html/body/div[2]/div[2]/div/div/div/article/div/div[1]/div/div/div[4]/ul/li #page number or https://cce.org.mx/blog/page/12/
# /html/body/div[2]/div[2]/div/div/div/article/div/div[2]/div[2]/div/div/div/a/div #categorias

# Otros Links
# https://cce.org.mx/blog/page/ #Hasta 12
# https://cce.org.mx/category/ #Los principales quedan abarcados en la barra de navegación dentro de Temas
# https://cce.org.mx/category/{category}/page/2/


# Dentro de category
# //*[@id="content"]/div #articulos
# //*[@id="nav-below"]/div[2]/div/div/div/a #numerospagina


# Dentro de sala de prensa https://cce.org.mx/sala-de-prensa/page/73/
# Comunicados
# /html/body/div[2]/div[2]/div/div/div/article/div[1]/div/div[3]/div/div/div[2]/h5/a#titulo
# /html/body/div[2]/div[2]/div/div/div/article/div[1]/div/div[4]/ul/li/a #numerospagina https://cce.org.mx/sala-de-prensa/page/{number}/
# Discursos
# //*[@id="ub-content-toggle-panel-0-1564b555-94e9-4a20-b5b1-c6596947248e"]/div/div/div[3]/div/div/div/h5/a FRANCISCO CERVANTES (2022-PRESENTE)
# hay mas de Francisco en la página 2, esto cambia en funcion de la página //*[@id="ub-content-toggle-panel-0-1564b555-94e9-4a20-b5b1-c6596947248e"]/div/div
# //*[@id="ub-content-toggle-panel-1-1564b555-94e9-4a20-b5b1-c6596947248e"]/div/div/div[3]/div/div/div/h5/a CARLOS SALAZAR LOMELÍN (2019-2022)
# //*[@id="ub-content-toggle-panel-0-ef5695b8-c503-43ac-b761-9d7950f23de8"]/div/div/div[3]/div/div/div/h5/a JUAN PABLO CASTAÑON CASTAÑON (2016-2019)
# //*[@id="ub-content-toggle-panel-0-b3b77186-bbc9-46c0-9cc1-c049a434288a"]/div/div/div[3]/div/div/div/h5/a GERARDO GUTIERREZ CANDIANI (2012-2015)


# Dentro de los artículos los hay con texto o con pdf
# (txt) https://cce.org.mx/2022/10/11/campana_deteccion_mas_accion/ || https://cce.org.mx/2022/10/05/primera_infancia_cce/
# (pdf) https://cce.org.mx/2022/08/18/el-sector-empresarial-reafirma-su-compromiso-con-la-lactancia-materna-y-la-primera-infancia/

# artículos con texto
# /html/body/div[2]/div[1]/div/div[1]/div/div[1]/img image
# /html/body/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div[2]/h1 titulo
# /html/body/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div[1]/a/span[2] secciones
# /html/body/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/span author
# /html/body/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div[3]/time publishing date
# //*[@id="post-5644"]/div/div/div/p text

# BÚSQUEDA EN LA PÁGINA
# POR KEYWORD EN EL SEARCH TOOL url/?s={palabra}
# POR FECHA url/2023/03/06/

# LINK QUE PARECE GENERAL PARA TODAS LAS SECCIONES
# //div/div/h3/a
