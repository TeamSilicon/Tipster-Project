#! this is where huge comparison goes b4 data is insterted into database
# from home.scrapers.statArena import stat_arena
# from difflib import SequenceMatcher

from django.template.defaultfilters import slugify

from home.models import Match
from home.scrapers.zulubet import zulubet
from django.core.management import call_command


def boiler(zulu_page, page, page2, today):
    zulubet_games = zulubet(zulu_page, today)
    # stat_arr_orign = stat_arena(page, today)
    # stat_arr = stat_arena(page, today)
    # featured_arr = stat_arena(page2, today)
    # print("Games One length: %s\nGames two length: %s" % (len(zulubet_games), len(stat_arr)))
    # success_compr = []
    # status = 0
    # for each2 in range(len(stat_arr)):
    # print("Outer Loop remaining %d" % len(stat_arr))
    # print("each2 in outer loop %s" % each2)
    # for each in range(len(zulubet_games)):
    # print("each in inner loop %s" % each)
    #   s = SequenceMatcher(
    #        None, zulubet_games[each][4], stat_arr[each2][4])
    #    if s.ratio() > 0.5:
    #         if SequenceMatcher(None, zulubet_games[each][1], stat_arr[each2][1]).ratio() > 0.6:
    #             # print("%s / %s  Efficiency %s" % (zulubet_games[each][4], stat_arr[each2][3], SequenceMatcher(None, zulubet_games[each][4], stat_arr[each2][3]).ratio()))
    #             if stat_arr[each2][3].strip() != "-:-":
    #                 res = stat_arr[each2][3]
    #             else:
    #                 res = zulubet_games[each][3]
    #             success_compr.append([zulubet_games[each][0], zulubet_games[each][1], "%s,%s" % (
    #                 zulubet_games[each][2], stat_arr[each2][2]), res, stat_arr[each2][4], zulubet_games[each][5], zulubet_games[each][6], stat_arr[each2][7]])
    #             # print("index for each %d" % each)
    #             del zulubet_games[each]
    #             # zulubet_games[each][4]+" looks like \n
    #             # print("index for each2 %d" % each2)
    #             status = 1
    #             break
    #         else:
    #             status = 0
    #     else:
    #         status = 0
    # print("Counter Level %d" % count)
    # print("status %d" % status)
    # if status == 1:
    #     # print("index for each2 outer %d" % each2)
    #     stat_arr[each2] = 'remv'
    #     status = 0
    # print("Inner Loop remaining %d" % len(zulubet_games))

    # print("Games that could be compared are %d out of %d" % (len(success_compr), len(stat_arr)))
    # stat_arr_clean = [x for x in stat_arr if x != "remv"]
    # print("Games one length unmatched: %s\nGames two length unmatched: %s" %(len(zulubet_games), len(stat_arr_clean)))
    # combined_games = zulubet_games + success_compr
    # + stat_arr_clean removed
    # for allgames

    for match in zulubet_games:
        Match.objects.update_or_create(
            slug=slugify(
                f'{match.get("date")}-{match.get("homeTeam")}-{match.get("awayTeam")}'),
            defaults=match
        )


    # call firestore update command
    call_command("firestore")

    # print("allgames done")
    # for tipGG
    # for each in stat_arr_orign:
        # outcome = getMatchStatus(each[6], each[3], 'bts')
        # if each[7]:
        #     TipGG.objects.update_or_create(
        #         slug=each[4],
        #         defaults={
        #             'date': each[0],
        #             'startTime': each[1],
        #             'teams': each[4],
        #             'pick': 'G-G',
        #             'odds': each[5],
        #             'result': each[3],
        #             'status': outcome
        #         })
        # for Over15
        # if each[8]:
        #     outcome = getMatchStatus(each[6], each[3], 1.5)
        #     Over15.objects.update_or_create(
        #         slug=each[4],
        #         defaults={
        #             'date': each[0],
        #             'startTime': each[1],
        #             'teams': each[4],
        #             'pick': 'Over 1.5',
        #             'odds': each[5],
        #             'result': each[3],
        #             'status': outcome
        #         })
        # # for Over25:
        # if each[9]:
        #     outcome = getMatchStatus(each[6], each[3], 2.5)
        #     Over25.objects.update_or_create(
        #         slug=each[4],
        #         defaults={
        #             'date': each[0],
        #             'startTime': each[1],
        #             'teams': each[4],
        #             'pick': 'Over 2.5',
        #             'odds': each[5],
        #             'result': each[3],
        #             'status': outcome
        #         })
        # # for Over35
        # if each[10]:
        #     outcome = getMatchStatus(each[6], each[3], 3.5)
        #     Over35.objects.update_or_create(
        #         slug=each[4],
        #         defaults={
        #             'date': each[0],
        #             'startTime': each[1],
        #             'teams': each[4],
        #             'pick': 'Over 3.5',
        #             'odds': each[5],
        #             'result': each[3],
        #             'status': outcome
        #         })
    # print("Big Thing done")
    # for Featured Games
    # for each in featured_arr:
        # Featured.objects.update_or_create(
        #     slug=each[4],
        #     defaults={
        #         'date': each[0],
        #         'startTime': each[1],
        #         'teams': each[4],
        #         'pick': each[2],
        #         'odds': each[5],
        #         'result': each[3],
        #         'status': each[6]
        #     })
    # print("Featured Games done")

# def getMatchStatus(outcome_text, result, case):
#     if outcome_text == "waiting":
#         return outcome_text
#     home_team_guest_team=[int(x) for x in result.split(":")]
#     if case != 'bts':
#         if sum(home_team_guest_team) > case:
#             return "won"
#         else:
#             return "lost"
#     else:
#         if 0 not in home_team_guest_team:
#             return "won"
#         else:
#             return "lost"
