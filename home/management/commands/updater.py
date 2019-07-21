from django.core.management.base import BaseCommand, CommandError
from apscheduler.schedulers.blocking import BlockingScheduler
from home.views import topnavselector
from datetime import timedelta
from home.boilerplate import boiler
from home.fetcher import requester

class Command(BaseCommand):
    help = 'Updates games in db'

    def handle(self, *args, **options):
        sched = BlockingScheduler()
        # print("nothing going on")
        @sched.scheduled_job('interval', minutes=1)
        # @sched.scheduled_job('interval', minutes=7)
        def update_games_today():
            print("Updating today Games")
            today = topnavselector()
            zulu_page = 'http://www.zulubet.com/tips-%d-%d-%d.html' % (today.day, today.month, today.year)
            arena_page ="https://www.statarea.com/predictions/date/%s-%s-%s/starttime" % (today.year, today.month, today.day)
            featured_page ="https://www.statarea.com/toppredictions/date/%s-%s-%s/" % (today.year, today.month, today.day)
            page_urls = [[zulu_page], [arena_page], [featured_page]]
            page_content1 = requester(page_urls[0], 1)
            page_content2 = requester(page_urls[1], 2)
            page_content3 = requester(page_urls[2], 3)
            boiler(page_content1, page_content2, page_content3, today)

        @sched.scheduled_job('interval', minutes=60)
        def update_games_yest():
            print("Updating Yesterday Games")
            today = topnavselector() + timedelta(days=-1)
            zulu_page = 'http://www.zulubet.com/tips-%d-%d-%d.html' % (today.day, today.month, today.year)
            arena_page ="https://www.statarea.com/predictions/date/%s-%s-%s/starttime" % (today.year, today.month, today.day)
            featured_page ="https://www.statarea.com/toppredictions/date/%s-%s-%s/" % (today.year, today.month, today.day)
            page_urls = [[zulu_page], [arena_page], [featured_page]]
            page_content1 = requester(page_urls[0], 1)
            page_content2 = requester(page_urls[1], 2)
            page_content3 = requester(page_urls[2], 3)
            boiler(page_content1, page_content2, page_content3, today)

        @sched.scheduled_job('interval', hours=3)
        def update_games_tom():
            print("Updating Tomorrow Games")
            today = topnavselector() + timedelta(days=1)
            zulu_page = 'http://www.zulubet.com/tips-%d-%d-%d.html' % (today.day, today.month, today.year)
            arena_page ="https://www.statarea.com/predictions/date/%s-%s-%s/starttime" % (today.year, today.month, today.day)
            featured_page ="https://www.statarea.com/toppredictions/date/%s-%s-%s/" % (today.year, today.month, today.day)
            page_urls = [[zulu_page], [arena_page], [featured_page]]
            page_content1 = requester(page_urls[0], 1)
            page_content2 = requester(page_urls[1], 2)
            page_content3 = requester(page_urls[2], 3)
            boiler(page_content1, page_content2, page_content3, today)

        sched.start()
