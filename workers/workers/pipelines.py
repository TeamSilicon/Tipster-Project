# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from home.models import ZuluBet


class WorkersPipeline(object):
    # def close_spider(self, spider):
        # And here we are saving our crawled data in django models.

    def process_item(self, item, spider):
        obj, created = ZuluBet.objects.update_or_create(
            teams=item['teams'],
            defaults={
                'match_date': item['match_date'],
                'time': item['time'],
                'teams': item['teams'],
                'tip': item['tip'],
                'tip_odd': item['tip_odd'],
                'ft_results': item['ft_results'],
            })
        return item
