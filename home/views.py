import datetime
from datetime import timedelta
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from home.models import AllGames, Featured,TipGG
from home.jackpot import possible_combinations
from home.boilerplate import boiler
from django.http import HttpResponse
import time
import requests


def topnavselector():
    date = datetime.date.today() # to get current date yy-mm-dd
    return date

def all_games(request):
    today, request_from, match_date = updater(request)
    games = AllGames.objects.filter(match_date=today).order_by('time', 'teams')
    return render(request, 'mysite/index.html',
                  {"games": games, "request_tom": request_from, "match_date": match_date})
def updater(request):
    print(request.path)
    if request.path == "/" or request.path == "/goalgoal/" or request.path == "/goalgoal/today/" or request.path == "/featured/" or request.path == "/featured/today/" or request.path == "/over/":
        today = topnavselector()
        request_from = 'today'
    elif request.path == "/tomorrow/" or request.path == "/goalgoal/tomorrow/" or request.path == "/featured/tomorrow/" or request.path == "/over/tomorrow/":
        today = topnavselector() + timedelta(days=1)
        request_from = 'tomorrow'
    elif request.path == "/yesterday/" or request.path == "/goalgoal/yesterday/" or request.path == "/featured/yesterday/" or request.path == "/over/yesterday":
        today = topnavselector() + timedelta(days=-1)
        request_from = 'yesterday'
    match_date = today.strftime("%d-%m").replace('-', '/')  # date when the match is played in / formart
    zulu_page = 'http://www.zulubet.com/tips-%d-%d-%d.html' % (today.day, today.month, today.year)
    arena_page ="https://www.statarea.com/predictions/date/%s-%s-%s/starttime" % (today.year, today.month, today.day)
    featured_page ="https://www.statarea.com/toppredictions/date/%s-%s-%s/" % (today.year, today.month, today.day)
    page_urls = [zulu_page, arena_page, featured_page]
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36' }
    page_names= []
    while True:
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
        if len(page_names) == 3:
            break
    boiler(page_names[0], page_names[1], page_names[2], today)
    return [today, request_from, match_date]


def goal_Goal(request):
    today, request_from, match_date =updater(request)
    games = TipGG.objects.filter(match_date=today).order_by('time', 'teams')
    return render(request, 'mysite/goalgoal.html', {
        "games": games, "request_tom": request_from, "match_date": match_date
        })

def featured(request):
    today, request_from, match_date = updater(request)
    games = Featured.objects.filter(match_date=today).order_by('time', 'teams')
    return render(request, 'mysite/featured.html', {
        "games": games, "request_tom": request_from, "match_date": match_date
        })


def jackpot(request):
    games = possible_combinations(['Kenya - Germany', 'Spain - Italia', 'Brazil - Spain'])
    print (len(games))
    return render(request, 'mysite/jackpot.html', {
        "games": games
        })

def over(request):
    today, request_from, match_date = updater(request)
    games = Over15.object.filter(match_date=today),order_by('time', 'teams')
    return render(request, 'mysite/over.html', {'games': games})

@csrf_exempt
def overtips(request):
    today, request_from, match_date = updater(request)
    if request.method == "POST" and request.is_ajax():
        selected_tab = request.POST.get('sel_tab', False)
        print
        if selected_tab == "over35":
            data = Over35.object.filter(match_date=today),order_by('time', 'teams')
            pick = " Over 3.5"
        elif selected_tab == "over25":
            data = Over25.object.filter(match_date=today),order_by('time', 'teams')
            pick = " Over 2.5"
        elif selected_tab == "over25":
            data = Over15.object.filter(match_date=today),order_by('time', 'teams')
            pick = " Over 1.5"
        else:
            data = "there was an error"
    else:
        data = "Not Safe"
    return HttpResponse([pick, data])

def slip(request):
    pass


# def game_detail(request, pk):
#     games_detail = get_object_or_404(AllGames, pk=pk)
#     return render(request, 'mysite/game_details.html', {'game': games_detail})
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
