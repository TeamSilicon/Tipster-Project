import requests
import bs4
import re

class CashBet:
    def __init__(self, page_url):
        self.page_url = page_url

    def procedure1(self):
        page = requests.get(self.page_url)
        game_info = []
        all_games = []
        try:
            page.raise_for_status()
        except Exception as error:
            print('There was a problem getting cash1 data: %s' % error)
        cash_soup = bs4.BeautifulSoup(page.text, 'html.parser')
        if type(cash_soup) == bs4.BeautifulSoup:
            games = cash_soup.findAll("span", style="background-color: white; color: #333333; font-family: AppYet-Regular-Sans; font-size: 16px;")
            games_num = len(games)
            print(games_num)
            # parsing data to method 2
            get_reg = re.compile(
                r'(.*?)\s*(12|1x|1|2|x2|x|(un|ov)\d+.\d+)\s*(@\d+.\d+)')
            for match in range(games_num):
                game_info.append(get_reg.findall(games[match].getText()))

        print(game_info)
        def empty(seq):
            try:
                return all(map(empty, seq))
            except TypeError:
                return False
        # if game_info is empty proceed to procedure2
        if empty(game_info):  # is empty ?
            all_games = self.procedure2(games)
        else:
            for group in game_info:
                for each in group:
                    if len(each) > 3:
                        all_games.append({
                            "league": ".....", "teams": each[0],
                            "tip": each[1], 'odds': each[3],
                            "time": "..."
                            })
        print("Printing from procedure1")
        return all_games

    def procedure2(self, game_info2):
        game_holder = []
        game_lib = []
        for each in game_info2:
            if each.getText() != '':
                game_holder.append(each.getText())

        if len(game_holder) == 66:
            print("That I know how to handle")
            for each_item in range(len(game_holder)):
                if each_item == 0:
                    # to be used later
                    # date = game_holder[each_item]
                    pass
                elif each_item == 1 or each_item == 6 or each_item == 11 or each_item == 16:
                    game_lib.append({
                        "league": game_holder[each_item],
                        "teams": game_holder[each_item+1],
                        "odds": game_holder[each_item+2],
                        "tip": game_holder[each_item+3],
                        "time": game_holder[each_item+4]
                    })
                elif each_item == 21 or each_item == 26 or each_item == 31 or each_item == 36 or each_item == 41:
                    game_lib.append({
                        "league": game_holder[each_item],
                        "teams": game_holder[each_item+1],
                        "odds": game_holder[each_item+2],
                        "tip": game_holder[each_item+3],
                        "time": game_holder[each_item+4]
                    })
                elif each_item == 46 or each_item == 51 or each_item == 56 or each_item == 61 or each_item == 61:
                    game_lib.append({
                        "league": game_holder[each_item],
                        "teams": game_holder[each_item+1],
                        "odds": game_holder[each_item+2],
                        "tip": game_holder[each_item+3],
                        "time": game_holder[each_item+4]
                    })
        else:
            print("I didn't get 66 games which I know how to handle")
        return game_lib
