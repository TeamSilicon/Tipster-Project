# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from home.models import ZuluBet


class WorkersPipeline(object):
    def __init__(self, teams, *args, **kwargs):
        self.teams = teams

    def close_spider(self, spider):
        # And here we are saving our crawled data in django models.
        obj, created = ZuluBet.objects.update_or_create(
            teams=self.teams,
            defaults={
                'match_date': self.match_date,
                'time': self.time,
                'teams': self.teams,
                'tip': self.tip,
                'tip_odd': self.tip_odd,
                'ft_results': self.ft_results
            })

    def process_item(self, item, spider):
        return item
