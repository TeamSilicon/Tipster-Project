from bs4 import BeautifulSoup
from itertools import chain
from home.results_overall import overall_result
from datetime import timedelta
import datetime

def stat_arena(page, match_date):
    games_store = []
    arena = BeautifulSoup(page.text, 'html.parser')
    if type(arena) == BeautifulSoup:
        games = arena.findAll(class_="match")
        games_num = len(games)
        for each in games:
            game_time = each.find(class_="date").getText().strip()
            game_time = datetime.datetime.strptime(game_time, "%H:%M")
            game_time = game_time + timedelta(hours=0)  # updating time to EAT
            game_time = game_time.strftime("%H:%M")
            tip = each.select(".tip > .value")[0].getText()
            hostteam = each.select(".hostteam > .name")[0].getText()
            guestteam = each.select(".guestteam > .name")[0].getText()
            teams = "%s - %s" % (hostteam, guestteam)
            try :
                hostscore = each.select(".hostteam > .goals")[0].getText()
                guestscore = each.select(".guestteam > .goals")[0].getText()
                score = "%s:%s" % (hostscore, guestscore)
                # print(each.select(".hostteam > .goals")[0].getText())
                # print(each.select(".guestteam > .goals")[0].getText())
            except AttributeError:
                print("from error" + each.select(".hostteam > .goals")[0].getText())
                print("from error" + each.select(".guestteam > .goals")[0].getText())
                guestscore=hostscore='-'
                score = ''
            bts = each.select('.coefbox.last')[1].getText().strip()
            gg_field = False
            if bts != '':
                try:
                    bts = 100 - int(bts)
                    if bts >=75:
                        # print(bts)
                        gg_field = True
                except ValueError as err:
                    print("bts value is not valid %s " % err)
            else:
                print("bts is blank : %s " % bts)
            results = score.split(":")
            if len(results) == 2 and hostscore !='-' and guestscore !='-':
                try:
                    result_home = int(results[0])
                    result_away = int(results[1])
                except ValueError:
                    result_home = 'post'
                    result_away = 'post'
            else:
                result_home = 'no_result'
                result_away = 'no_result'
            tipx_odd=tip1_odd=tip2_odd="0"  # making odd zero by default
            outcome, tip_odd = overall_result(result_home, result_away, tip, tipx_odd,tip1_odd,tip2_odd)
            # print([match_date, game_time, tip, score, teams, tip_odd, outcome]) # for testing
            games_store.append([match_date, game_time, tip, score, teams, tip_odd, outcome, gg_field])
        return games_store
    else:
        return "not bs4 obj"
