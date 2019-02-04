import re
import scrapy
import datetime
from bs4 import BeautifulSoup
from datetime import timedelta
from scrapy.http import Request


class ZuluBet(scrapy.Spider):
    name = "zulubet"
    # We are going to pass these args from our django view.
    # To make everything dynamic, we need to override them inside __init__ method

    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url')or kwargs.get('domain')
        print("Dennoh Was here again %s" % self.url)

    def start_requests(self):
        return [Request(self.url, callback=self.parse, dont_filter=True)]

    def parse(self, response):
        # Getting only table rows with bgcolor property
        tr_elems = response.css('tr[bgcolor]').extract()
        print("Today games are " + str(len(tr_elems)))  # number of games
        error_games = []  # to store games that couldn't be parsed
        # Extracting games
        removing_mf_usertime = re.compile(r'^mf_usertime(.*);')
        empty_games_counter = 0
        for gameNo in range(len(tr_elems)):
            team = removing_mf_usertime.sub(
                '',  BeautifulSoup(tr_elems[gameNo], 'html.parser').getText())
            groupings_trial = re.compile(r'''(
            \d+-\d+,\s)    # match_date
            (\d+:\d+\s)    # time
            ([\w+\W+]*(\s\w+)*\s-\s\w+[^1:]*)  #teams
            ([\d+]*[\s\w+]*1:\s+\d+%)*   # 1
            (X:\s+\d+%)*   # X
            (2:\s+\d+%)*   # 2
            (\d+%\d+%\d+%)   #
            (12|1X|1|2|X2|X)      # tip
            (\d[^1:])*
            ([1:\s\d+.\d+]+[^X:]*)  # prob1
            (X:\s\d+.\d{2})         # probX
            (2:\s\d+.\d{2})         # prob2
            (\d+.\d+.\d+.\d{2})
            (\d+:\d+|[\s-]*)              # result
            ''', re.VERBOSE)
            game_info = groupings_trial.findall(team)
            if len(game_info) < 1:
                empty_games_counter += 1
                error_games += ["empty list"]
                # print(tr_elems[0+gameNo].getText())
                # if games_info list is not empty
                print(str(empty_games_counter)+" Games could not be parsed")
            else:
                match_date = game_info[0][0].strip()
                game_time = game_info[0][1].strip()
                formatted_time = datetime.datetime.strptime(game_time, "%H:%M")
                formatted_time = formatted_time + timedelta(hours=2)
                start_time = formatted_time.strftime("%H:%M")
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

                result_home = str(result_home)
                result_away = str(result_away)

                def overall_result():
                    if result_home == 'no_result' or result_away == 'no_result':
                        win_odd = 0.0
                        if game_info[0][8] == 'X':
                            win_odd = game_info[0][11].split(":")[1]
                        elif game_info[0][8] == '1':
                            win_odd = game_info[0][10].split(":")[1]
                        elif game_info[0][8] == '2':
                            win_odd = game_info[0][12].split(":")[1]
                        elif game_info[0][8] == '12':
                            win_odd = 0
                            # get odd for double chance
                        elif game_info[0][8] == '1X':
                            win_odd = 0

                            # get odd for double chance
                        elif game_info[0][8] == 'X2':
                            win_odd = 0
                            # get odd for double chance
                        return ['no_results_yet', win_odd]
                    else:
                        if game_info[0][8] == 'X':
                            win_odd = game_info[0][11].split(":")[1]
                            if result_home == result_away:
                                return ['drawwin', win_odd]
                            else:
                                return ['drawlose', win_odd]
                        elif game_info[0][8] == '1':
                            win_odd = game_info[0][10].split(":")[1]
                            if result_home > result_away:
                                return ['homewin', win_odd]
                            else:
                                return ['homelose', win_odd]
                        elif game_info[0][8] == '2':
                            win_odd = game_info[0][12].split(":")[1]
                            if result_away > result_home:
                                return ['awaywin', win_odd]
                            else:
                                return ['awaylose', win_odd]
                        elif game_info[0][8] == '12':
                            win_odd = 0
                            if result_away != result_home:
                                return ['12win', win_odd]
                            else:
                                return ['12lose', win_odd]
                        elif game_info[0][8] == '1X':
                            win_odd = 0
                            if result_home >= result_away:
                                return ['1Xwin', win_odd]
                            else:
                                return ['1Xlose', win_odd]
                        elif game_info[0][8] == 'X2':
                            win_odd = 0
                            if result_home <= result_away:
                                return ['X2win', win_odd]
                            else:
                                return ['X2lose', win_odd]
                yield {
                    'match_date': match_date,
                    'time': start_time,
                    'teams': game_info[0][2],
                    'tip': game_info[0][8],
                    'tip_odd': overall_result()[1],
                    'ft_results': overall_result()[0]
                    }
