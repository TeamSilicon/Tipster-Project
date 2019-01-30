import scrapy
import re


class ZuluBet(scrapy.Spider):
    name = "zulubet"

    start_urls = [
        'http://www.zulubet.com/',
    ]

    def parse(self, response):
        # Getting only table rows with bgcolor property
        tr_elems = response.css('tr[bgcolor]').extract()
        print("Today games are " + str(len(tr_elems)))  # number of games
