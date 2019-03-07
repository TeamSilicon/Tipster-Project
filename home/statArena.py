from bs4 import BeautifulSoup
from itertools import chain
import requests
import re

def stat_arena():
    page = requests.get("https://www.statarea.com/predictions")
    games_store = []
    try:
        page.raise_for_status()
    except Exception as error:
        print('There was a problem getting cash1 data: %s' % error)
    arena = BeautifulSoup(page.text, 'html.parser')
    if type(arena) == BeautifulSoup:
        games = arena.findAll(class_="cmatch")
        games_num = len(games)
        get_algo = re.compile(
        r'(\d+:\d+)\s+(12|1X|1|2|X2|X)(\d+:\d+)*(.*)')
        for each in games:
            games_store.append(list(chain(*get_algo.findall(each.getText()))))
        return games_store
    else:
        return "not bs4 obj"
