import requests
import datetime
import bs4
import re
from datetime import timedelta
from home.models import AllGames
# from .send_mail import send_mail


class ZuluGames:
    def __init__(self, page_url, match_date):
        self.page_url = page_url
        self.match_date = match_date  # date when the match is played

    def zulu_procedure(self):
        zulu_page = requests.get(self.page_url)
        games_collec = []
        try:
            zulu_page.raise_for_status()
        except Exception as error:
            print('There was a problem getting web data: %s' % error)

        zulu_soup = bs4.BeautifulSoup(zulu_page.content, 'html.parser')
        if type(zulu_soup) == bs4.BeautifulSoup:
            tr_elems = zulu_soup.findAll("tr", bgcolor=re.compile('^#.*'))
            games_number = len(tr_elems)
            print("Today games are " + str(games_number))
            if games_number != 0:
                error_games = [] # Games that could not be parsed
                # Extracting games
                removing_mf_usertime = re.compile(r'^mf_usertime(.*);')
                empty_games_counter = 0
                for gameNo in range(games_number):
                    team = removing_mf_usertime.sub('', tr_elems[gameNo].getText())
                    groupings_trial = re.compile(r'''(
                    \d+-\d+,\s)                                                       #date
                    (\d+:\d+\s)                                                       #time
                    ([\w+\W+]*(\s\w+)*\s-\s\w+[^1:]*)              #teams
                    ([\d+]*[\s\w+]*1:\s+\d+%)*   #1
                    (X:\s+\d+%)*   #X
                    (2:\s+\d+%)*   #2
                    (\d+%\d+%\d+%)   #
                    (12|1X|1|2|X2|X)      #chance
                    (\d[^1:])*
                    ([1:\s\d+.\d+]+[^X:]*)  #prob1
                    (X:\s\d+.\d{2})         #probX
                    (2:\s\d+.\d{2})         #prob2
                    (\d+.\d+.\d+.\d{2})
                    (\d+:\d+|[\s-]*)              #result
                    ''', re.VERBOSE)
                    game_info = groupings_trial.findall(team)
                    if len(game_info) < 1:
                        empty_games_counter += 1
                        error_games += ["empty list"]
                        # print(tr_elems[0+gameNo].getText())
                        # if games_info list is not empty
                        print(str(empty_games_counter)+" Games could not be parsed")
                    else:
                        game_time = game_info[0][1].strip() # updating time to EAT
                        full_date = datetime.datetime.strptime(game_time, "%H:%M")
                        full_date = full_date + timedelta(hours=0)
                        formatted_time = full_date.strftime("%H:%M")
                        try:
                            results = game_info[0][14].split(':')
                            if len(results) == 2:
                                result_home = int(results[0])
                                result_away = int(results[1])
                            else:
                                result_home = 'no_result'
                                result_away = 'no_result'
                        except Exception as no_score:
                                # Adding to error games that there was no result
                                error_games += [no_score]

                        outcome, tip_odd = overall_result(result_home, result_away, game_info[0][8], game_info[0][11], game_info[0][10], game_info[0][12])
                                                # game date        game time     ,   #tip         # score       ,    #names       ,   "game odds",        "results"
                        games_collec.append([self.match_date, formatted_time, game_info[0][8], game_info[0][14], game_info[0][2], str(tip_odd).strip(), outcome])
        return games_collec
        #         # send_mail(len(error_games))
