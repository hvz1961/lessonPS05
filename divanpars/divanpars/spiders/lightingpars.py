import scrapy


class LightingparsSpider(scrapy.Spider):
    name = "lightingpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lamp = response.css("div.LlPhw")
        for lamp in lamp:
            yield {
                "name" : lamp.css("div.lsooF span::text").get(),
                "price" : lamp.css("div.pY3d2 span::text").get(),
                "url" : lamp.css("a").attrib["href"],

            }

