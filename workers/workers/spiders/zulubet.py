import scrapy
import re


class ZuluBet(scrapy.Spider):
    name = "zulubet"

    start_urls = [
        'http://www.zulubet.com/',
    ]

    def parse(self, response):
        tr_elems = response.css("tr", bgcolor=re.compile('^#.*')).extract()
