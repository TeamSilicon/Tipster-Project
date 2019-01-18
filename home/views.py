import datetime
from datetime import timedelta

from django.shortcuts import render, get_object_or_404
from .models import Prono
from .cashbetting import CashBet
from .zulubet import ZuluBet


def topnavselector():
    date = datetime.datetime.now()

    return date


def homepage_today(request):
    today = topnavselector()
    res = 'http://www.zulubet.com/tips-%d-%d-%d.html' % (today.day, today.month, today.year)
    match_date = today.strftime("%d-%m")  # date when the match is played
    games = ZuluBet(res, match_date).zulu_procedure()
    request_from = "tod"
    print(res)
    return render(request, 'mysite/index.html',
                  {"games": games, "request_tom": request_from})


def yesterday(request):
    today = topnavselector() - timedelta(days=1)
    res = 'http://www.zulubet.com/tips-%d-%d-%d.html' % (today.day, today.month, today.year)
    match_date = today.strftime("%d-%m")  # date when the match is played
    games = ZuluBet(res, match_date).zulu_procedure()
    request_from = "yest"
    print(res)
    return render(request, 'mysite/index.html',
                  {"games": games, "request_tom": request_from})


def tomorrow(request):
    today = topnavselector() + timedelta(days=1)
    res = 'http://www.zulubet.com/tips-%d-%d-%d.html' % (today.day, today.month, today.year)
    match_date = today.strftime("%d-%m")  # date when the match is played
    games = ZuluBet(res, match_date).zulu_procedure()
    request_from = "tom"
    print(res)
    return render(request, 'mysite/index.html', {"games": games, "request_tom": request_from })


month = {
    1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june",
    7: "july", 8: "august", 9: "september", 10: "october", 11: "november",
    12: "december"
    }


def featured(request):
    today = topnavselector()
    # page_url = "http://cashbettingtips.blogspot.com/2019/01/11-january.html"
    page_url = 'http://cashbettingtips.blogspot.com/%d/0%d/%d-%s.html' % (today.year, today.month, today.day, month[today.month])
    # match_date = today.strftime("%d-%m")  # date when the match is played
    games_dict = CashBet(page_url).procedure1()
    request_from = "tod"
    return render(request, 'mysite/featured.html', {
        "games": games_dict, "request_tom": request_from
        })


def game_details(request, pk):
    games_detail = get_object_or_404(Prono, pk=pk)
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
