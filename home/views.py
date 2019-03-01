import datetime
from datetime import timedelta
from django.shortcuts import render, get_object_or_404
from home.models import ZuluBet
from home.cashbetting import CashBet
from home.zulubet import ZuluGames


def topnavselector():
    date = datetime.datetime.now()
    return date


def all_games(request):
    if request.path == "/":
        today = topnavselector()
        request_from = 'today'
    elif request.path == "/tomorrow/":
        today = topnavselector() + timedelta(days=1)
        request_from = 'tomorrow'
    elif request.path == "/yesterday/":
        today = topnavselector() + timedelta(days=-1)
        request_from = 'yesterday'
    match_date = today.strftime("%d-%m").replace('-', '/')  # date when the match is played in / formart
    url = 'http://www.zulubet.com/tips-%d-%d-%d.html' % (today.day, today.month, today.year)
    games = ZuluGames(url, today).zulu_procedure
    return render(request, 'mysite/index.html',
                  {"games": games, "request_tom": request_from, "match_date": match_date})


month = {
    1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june",
    7: "july", 8: "august", 9: "september", 10: "october", 11: "november",
    12: "december"
    }


def featured(request):
    today = topnavselector()
    # page_url = "http://cashbettingtips.blogspot.com/2019/01/11-january.html"
    page_url = 'http://cashbettingtips.blogspot.com/%d/%s/%d-%s.html' % (today.year, str(today.month).zfill(2), today.day, month[today.month])
    # match_date = today.strftime("%d-%m")  # date when the match is played
    games_dict = CashBet(page_url).procedure1()
    request_from = "tod"
    return render(request, 'mysite/featured.html', {
        "games": games_dict, "request_tom": request_from
        })

def goal_Goal(request):
    pass

def jackpot(request):
    pass

def overTips(request):
    pass

def slip(request):
    pass


def game_detail(request, pk):
    games_detail = get_object_or_404(ZuluBet, pk=pk)
    return render(request, 'mysite/game_details.html', {'game': games_detail})
# no risk no reward


def comingsoon(request):
    return render(request, 'mysite/comingsoon.html')


def login(request):
    return render(request, 'mysite/login.html')


def error_404(request):
    data = {}
    return render(request, 'mysite/error_404.html', {'data': data})


def error_500(request):
    data = {}
    return render(request, 'mysite/error_505.html', {'data': data})
