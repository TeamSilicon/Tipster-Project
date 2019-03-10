from bs4 import BeautifulSoup
from itertools import chain
from home.results_overall import overall_result
import re

def stat_arena(page, match_date):
    games_store = []
    arena = BeautifulSoup(page.text, 'html.parser')
    if type(arena) == BeautifulSoup:
        games = arena.findAll(class_="cmatch")
        games_num = len(games)
        get_algo = re.compile(
        r'''(
        \d+:\d+)\s+   # time
        (12|1X|1|2|X2|X)* # tip
        (\s*\d+\s*:\d+\s*)*     # outcome
        (.*)   # team names
        ''', re.VERBOSE)
        for each in games:
            b = list(chain(*get_algo.findall(each.getText())))
            b[0:0] = [match_date]  # inserting date
            results =  b[3].split(":")
            if len(results) == 2:
                result_home = int(results[0])
                result_away = int(results[1])
            else:
                result_home = 'no_result'
                result_away = 'no_result'
            tip=b[2]
            tipx_odd=tip1_odd=tip2_odd="0:0"  # making odd zero by default
            outcome, tip_odd = overall_result(result_home, result_away, tip, tipx_odd,tip1_odd,tip2_odd)
            b[5:5] = [tip_odd]  # inserting tip_odd # 0.0
            b[6:6] = [outcome]  # determining which team which won
            games_store.append(b)
        return games_store
    else:
        return "not bs4 obj"
