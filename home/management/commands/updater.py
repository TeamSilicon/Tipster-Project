from django.core.management.base import BaseCommand, CommandError
from apscheduler.schedulers.blocking import BlockingScheduler
from home.views import date_picker
from home.boilerplate import boiler
from home.fetcher import requester
from django.conf import settings


class Command(BaseCommand):
    help = 'Initiates scrapers to get games'

    def handle(self, *args, **options):
        sched = BlockingScheduler()

        @sched.scheduled_job('interval', minutes=settings.TODAY_FETCH_INTERVAL_MINS)
        def update_games_today():
            today = date_picker()
            print(f"Updating today Games - {today}")
            zulu_page = 'http://www.zulubet.com/tips-%d-%d-%d.html' % (
                today.day, today.month, today.year)
            arena_page = "https://www.statarea.com/predictions/date/%s-%s-%s/starttime" % (
                today.year, today.month, today.day)
            featured_page = "https://www.statarea.com/toppredictions/date/%s-%s-%s/" % (
                today.year, today.month, today.day)
            page_urls = [[zulu_page], [arena_page], [featured_page]]
            page_content1 = requester(page_urls[0], 1)
            page_content2 = requester(page_urls[1], 2)
            page_content3 = requester(page_urls[2], 3)
            boiler(page_content1, page_content2, page_content3, today)

        @sched.scheduled_job('interval', minutes=settings.YEST_FETCH_INTERVAL_MINS)
        def update_games_yest():
            print("Updating Yesterday Games")
            today = date_picker(-1)
            zulu_page = 'http://www.zulubet.com/tips-%d-%d-%d.html' % (
                today.day, today.month, today.year)
            arena_page = "https://www.statarea.com/predictions/date/%s-%s-%s/starttime" % (
                today.year, today.month, today.day)
            featured_page = "https://www.statarea.com/toppredictions/date/%s-%s-%s/" % (
                today.year, today.month, today.day)
            page_urls = [[zulu_page], [arena_page], [featured_page]]
            page_content1 = requester(page_urls[0], 1)
            page_content2 = requester(page_urls[1], 2)
            page_content3 = requester(page_urls[2], 3)
            boiler(page_content1, page_content2, page_content3, today)

        @sched.scheduled_job('interval', minutes=settings.TMRW_FETCH_INTERVAL_MINS)
        def update_games_tom():
            print("Updating Tomorrow Games")
            today = date_picker(1)
            zulu_page = 'http://www.zulubet.com/tips-%d-%d-%d.html' % (
                today.day, today.month, today.year)
            arena_page = "https://www.statarea.com/predictions/date/%s-%s-%s/starttime" % (
                today.year, today.month, today.day)
            featured_page = "https://www.statarea.com/toppredictions/date/%s-%s-%s/" % (
                today.year, today.month, today.day)
            page_urls = [[zulu_page], [arena_page], [featured_page]]
            page_content1 = requester(page_urls[0], 1)
            page_content2 = requester(page_urls[1], 2)
            page_content3 = requester(page_urls[2], 3)
            boiler(page_content1, page_content2, page_content3, today)

        sched.start()
