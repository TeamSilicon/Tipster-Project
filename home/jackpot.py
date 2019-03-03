from itertools import product

def possible_combinations(games):
    game_keys = []
    game_store = []
    for i, res in enumerate(product('1x2', repeat=len(games)), 1):
        game_keys.append(i)
        for gr in zip(games, res):
            game_store.append('{} {}'.format(*gr))
    return game_store
