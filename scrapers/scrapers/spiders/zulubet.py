import scrapy


class ZuluBet(scrapy.Spider):
    name = "zulubet"

    start_urls = [
        'http://www.zulubet.com/',
    ]

    def parse(self, response):
        pass
