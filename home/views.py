import datetime
from datetime import timedelta
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from home.models import AllGames, Featured, TipGG, Over35, Over25, Over15
from home.jackpot import possible_combinations
from django.http import HttpResponse
from home.c2b import C2B


def date_picker(days=0):
    date = datetime.date.today()  # to get current date yy-mm-dd
    return date + timedelta(days)


def all_games(request):
    today, request_from, date = updater(request)
    games = AllGames.objects.filter(date=today).order_by('start_time', 'teams')
    context = {"games": games, "request_tom": request_from,
               "date": date}
    return render(request, 'index.html', context)


def updater(request):
    if request.path == "/" or request.path == "/goalgoal/" or request.path == "/goalgoal/today/" or request.path == "/featured/" or request.path == "/featured/today/" or request.path == "/over/" or request.path == "/over/today/":
        today = date_picker()
        request_from = 'today'
    elif request.path == "/tomorrow/" or request.path == "/goalgoal/tomorrow/" or request.path == "/featured/tomorrow/" or request.path == "/over/tomorrow/":
        today = date_picker() + timedelta(days=1)
        request_from = 'tomorrow'
    elif request.path == "/yesterday/" or request.path == "/goalgoal/yesterday/" or request.path == "/featured/yesterday/" or request.path == "/over/yesterday/":
        today = date_picker() + timedelta(days=-1)
        request_from = 'yesterday'
    # date when the match is played in / formart
    date = today.strftime("%d-%m").replace('-', '/')
    return [today, request_from, date]


def goal_Goal(request):
    today, request_from, date = updater(request)
    games = TipGG.objects.filter(date=today).order_by('start_time', 'teams')
    return render(request, 'goalgoal.html', {
        "games": games, "request_tom": request_from, "date": date
    })


def featured(request):
    today, request_from, date = updater(request)
    games = Featured.objects.filter(date=today).order_by('start_time', 'teams')
    return render(request, 'featured.html', {
        "games": games, "request_tom": request_from, "date": date
    })


def jackpot(request):
    games = possible_combinations(
        ['Kenya - Germany', 'Spain - Italia', 'Brazil - Spain'])
    # print (len(games))
    return render(request, 'jackpot.html', {
        "games": games
    })


def over(request):
    today, request_from, date = updater(request)
    over15 = Over15.objects.filter(date=today).order_by('start_time', 'teams')
    over25 = Over25.objects.filter(date=today).order_by('start_time', 'teams')
    over35 = Over35.objects.filter(date=today).order_by('start_time', 'teams')
    context = {'over15': over15, 'over25': over25, 'over35': over35,
               'request_tom': request_from, 'date': date}
    return render(request, 'over.html', context)


def slip(request):
    pass


def notify(request):
    return render(request, 'comingsoon.html')


def c2b_payment_request(request):
    c2b = C2B()
    access_token = c2b.access_token()
    print('-----------Received Acces Token-----------')
    c2b.register_url(access_token)
    print('-----------Registered Url-----------')
    r = c2b.request_payment(access_token, 100, 254715605476)
    return render(request, 'comingsoon.html')


def c2b_validation_callback(request):
    c2b = C2B()
    response = request.json()
    return c2b.validate_payment(response)


def c2b_confirmation_callback(request):
    c2b = C2B()
    response = request.json()
    return c2b.confirm_payment(response)


def comingsoon(request):
    return render(request, 'comingsoon.html')


def login(request):
    return render(request, 'login.html')


def error_404(request):
    data = {}
    return render(request, 'error_404.html', {'data': data})


def error_500(request):
    data = {}
    return render(request, 'error_505.html', {'data': data})

