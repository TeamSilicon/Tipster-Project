from apscheduler.schedulers.background import BackgroundScheduler
from home.views import topnavselector
from datetime import timedelta
from home.boilerplate import boiler
from home.fetcher import requester
sched = BackgroundScheduler()

@sched.scheduled_job('interval', minutes=15)
def update_games_today():
    today = topnavselector()
    zulu_page = 'http://www.zulubet.com/tips-%d-%d-%d.html' % (today.day, today.month, today.year)
    arena_page ="https://www.statarea.com/predictions/date/%s-%s-%s/starttime" % (today.year, today.month, today.day)
    featured_page ="https://www.statarea.com/toppredictions/date/%s-%s-%s/" % (today.year, today.month, today.day)
    page_urls = [[zulu_page], [arena_page], [featured_page]]
    page_content1 = requester(page_urls[0], 1)
    page_content2 = requester(page_urls[1], 2)
    page_content3 = requester(page_urls[2], 3)
    boiler(page_content1, page_content2, page_content3, today)

@sched.scheduled_job('interval', hours=6)
def update_games_yest():
    today = topnavselector() + timedelta(days=-1)
    zulu_page = 'http://www.zulubet.com/tips-%d-%d-%d.html' % (today.day, today.month, today.year)
    arena_page ="https://www.statarea.com/predictions/date/%s-%s-%s/starttime" % (today.year, today.month, today.day)
    featured_page ="https://www.statarea.com/toppredictions/date/%s-%s-%s/" % (today.year, today.month, today.day)
    page_urls = [[zulu_page], [arena_page], [featured_page]]
    page_content1 = requester(page_urls[0], 1)
    page_content2 = requester(page_urls[1], 2)
    page_content3 = requester(page_urls[2], 3)
    boiler(page_content1, page_content2, page_content3, today)

@sched.scheduled_job('interval', hours=6)
def update_games_tom():
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
