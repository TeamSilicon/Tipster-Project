from itertools import product

def possible_combinations(games):
    game_store = {}
    for i, res in enumerate(product('1x2', repeat=len(games)), 1):
        for gr in zip(games, res):
            game_store[i] = '{} {}'.format(*gr)
    return game_store
