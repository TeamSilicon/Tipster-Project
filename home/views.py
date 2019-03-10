import datetime
from datetime import timedelta
from django.shortcuts import render, get_object_or_404
from home.models import AllGames
from home.cashbetting import CashBet
from home.jackpot import possible_combinations
from home.boilerplate import boiler
import time
import requests


def topnavselector():
    date = datetime.date.today() # to get current date yy-mm-dd
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
    zulu_page = 'http://www.zulubet.com/tips-%d-%d-%d.html' % (today.day, today.month, today.year)
    arena_page ="https://www.statarea.com/predictions/date/%s-%s-%s/starttime" % (today.year, today.month, today.day)
    page_urls = [zulu_page, arena_page]
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36' }
    page_names = []

    while False:
        page_names= []
        for index, page in  enumerate(page_urls):
            try:
                page_name = requests.get(page, headers=headers, timeout=10)
                try:
                    page_name.raise_for_status()
                except Exception as error:
                    print('There was a problem getting web data: %s' % error)
                if page_name.status_code != 200:
                    print('There was a problem getting web data: %s' % error)
                    break
                print("Page %d done!!!. Proceeding to the next trial" % index)
                page_names.append(page_name)
            except requests.ConnectionError as e:
                print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
                print(str(e))
                time.sleep(4) # wait 4 seconds before we make the next request
                break
            except requests.Timeout as e:
                print("OOPS!! Timeout Error")
                print(str(e))
                time.sleep(4) # wait 4 seconds before we make the next request
                break
            except requests.RequestException as e:
                print("OOPS!! General Error")
                print(str(e))
                time.sleep(4) # wait 4 seconds before we make the next request
                break
            except KeyboardInterrupt:
                print("Someone closed the program")
        if len(page_names) == 2:
            break

    # boiler(page_names[0], page_names[1], today)
    games = AllGames.objects.filter(match_date=today).order_by('time', 'teams')
    return render(request, 'mysite/index.html',
                  {"games": games, "request_tom": request_from, "match_date": match_date})

def goal_Goal(request):
    if request.path == "/goalgoal/" or request.path == "/goalgoal/today/":
        today = topnavselector()
        request_from = 'today'
    elif request.path == "/goalgoal/tomorrow/":
        today = topnavselector() + timedelta(days=1)
        request_from = 'tomorrow'
    elif request.path == "/goalgoal/yesterday/":
        today = topnavselector() + timedelta(days=-1)
        request_from = 'yesterday'
    games = AllGames.objects.filter(tipGG=True, match_date=today).order_by('time', 'teams')
    return render(request, 'mysite/goalgoal.html', {
        "games": games, "request_tom": request_from
        })

month = {
    1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june",
    7: "july", 8: "august", 9: "september", 10: "october", 11: "november",
    12: "december"
    }


def featured(request):
    today = topnavselector()
    page_url = "http://cashbettingtips.blogspot.com/2018/12/01-january.html"
    # page_url = 'http://cashbettingtips.blogspot.com/%d/%s/%s-%s.html' % (today.year, str(today.month).zfill(2), str(today.day).zfill(2), month[today.month])
    # match_date = today.strftime("%d-%m")  # date when the match is played
    games_dict = CashBet(page_url).procedure1()
    request_from = "tod"
    return render(request, 'mysite/featured.html', {
        "games": games_dict, "request_tom": request_from
        })


def jackpot(request):
    games = possible_combinations(['Kenya - Germany', 'Spain - Italia', 'Brazil - Spain'])
    print (len(games))
    return render(request, 'mysite/jackpot.html', {
        "games": games
        })


def overTips(request):
    pass

def slip(request):
    pass


def game_detail(request, pk):
    games_detail = get_object_or_404(AllGames, pk=pk)
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
