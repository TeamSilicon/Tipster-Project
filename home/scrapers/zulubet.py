import datetime
from datetime import timedelta

import bs4

from home.models import Match
from home.results_overall import overall_result


def zulubet(page, match_date):
    games_collec = []
    zulu_soup = bs4.BeautifulSoup(page.content, 'html.parser')
    tr_elems = zulu_soup.find_all("tr", {'bgcolor': ['#FFFFFF', '#EFEFEF']})
    games_number = len(tr_elems)
    error_games = []  # Games that could not be parsed
    if games_number != 0:
        for tr in tr_elems:  # Extracting games
            try:
                # print(tr.select('td > noscript')[0].getText())
                try:
                    date, time = tr.select('td > noscript')[
                        0].getText().split(",")
                except ValueError:
                    # print("I have been fixed")
                    time = tr.select('td > noscript')[0].getText()
                teams = tr.find_all('td')[1].getText()
                print(teams)
                homeTeam, awayTeam = teams.split(' - ')
                tip = tr.select("td > font > b")[0].getText()
                home_team_odd = tr.find_all('td', class_="aver_odds_full")[
                    0].getText().strip()
                draw_odd = tr.find_all('td', class_="aver_odds_full")[
                    1].getText().strip()
                away_odd = tr.find_all('td', class_="aver_odds_full")[
                    2].getText().strip()
                result = tr.find_all(
                    'td', align="center")[-1].getText().strip()
            except IndexError:
                error_games.append(tr)

            game_time = time.strip()  # updating time to EAT
            full_date = datetime.datetime.strptime(game_time, "%H:%M")
            full_date = full_date + timedelta(hours=3)
            startTime = full_date.strftime("%H:%M")
            results = result.split(':')
            if len(results) == 2 and '-' not in results:
                result_home = int(results[0])
                result_away = int(results[1])
            else:
                result = "-:-"
                result_home = 'no_result'
                result_away = 'no_result'
            if tip == "" and home_team_odd != "" and away_odd != "" and draw_odd != "":  # Quickfix for where tip is none
                tip_dict = {'home_team_odd': float(home_team_odd), "away_odd": float(
                    away_odd), "draw_odd": float(draw_odd)}
                tip_dict = sorted(tip_dict.items(), key=lambda k: k[1])
                if tip_dict[0][0] == "draw_odd":
                    tip = "X"
                elif tip_dict[0][0] == "home_team_odd":
                    tip = "1X"
                elif tip_dict[0][0] == "away_odd":
                    tip = 'X2'
            # print("%s, %s, %s, %s, %s, %s" %(result_home, result_away, tip, draw_odd, home_team_odd, away_odd))
            outcome, odds = overall_result(
                result_home, result_away, tip, draw_odd, home_team_odd, away_odd)
            games_collec.append(
                {"date": match_date,
                 "startTime": startTime,
                 "pick": tip,
                 "result": result,
                 "homeTeam": homeTeam.strip(),
                 "awayTeam": awayTeam.strip(),
                 "odds": odds,
                 "status": outcome
                 }
            )

    # print("%d Games could not be parsed" % len(error_games))
    # print(error_games)
    # print("Today games are " + str(games_number-len(error_games)))
    return games_collec
