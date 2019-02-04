# scrapy api
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def zulu_spider(url):
    # starting zulu spider
    crawler = CrawlerProcess(get_project_settings())
    crawler.crawl('zulubet', url=url)
    crawler.start()  # block here until the crawling is finished
