from bs4 import BeautifulSoup
from itertools import chain
from home.results_overall import overall_result
from datetime import timedelta
import datetime

def stat_arena(page, match_date):
    games_store = []
    arena = BeautifulSoup(page.text, 'html.parser')
    if type(arena) == BeautifulSoup:
        games = arena.findAll(class_="cmatch")
        games_num = len(games)
        for each in games:
            game_time = each.find(class_="time").getText().strip()
            game_time = datetime.datetime.strptime(game_time, "%H:%M")
            game_time = game_time + timedelta(hours=2)  # updating time to EAT
            game_time = game_time.strftime("%H:%M")
            tip = each.find(class_="tip").getText()
            teams = each.find(class_="teams").getText()
            print(teams)
            try :
                score = each.find(class_="result").getText().strip()
            except AttributeError:
                score = "none"
            results = score.split(":")
            if len(results) == 2 and score !="none":
                try:
                    result_home = int(results[0])
                    result_away = int(results[1])
                except ValueError:
                    result_home = 'no_result'
                    result_away = 'no_result'
            else:
                result_home = 'no_result'
                result_away = 'no_result'
            tipx_odd=tip1_odd=tip2_odd="0:0"  # making odd zero by default
            outcome, tip_odd = overall_result(result_home, result_away, tip, tipx_odd,tip1_odd,tip2_odd)
            games_store.append([match_date, game_time, tip, score, teams, tip_odd, outcome])
        return games_store
    else:
        return "not bs4 obj"
