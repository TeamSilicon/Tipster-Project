#! this is where huge comparison goes b4 data is insterted into database
from home.statArena import stat_arena
from home.zulubet import zulu_procedure
from home.models import Match
from difflib import SequenceMatcher

def boiler(zulu_page, page, page2, today):
    zulu_arr = zulu_procedure(zulu_page, today)
    stat_arr_orign = stat_arena(page, today)
    stat_arr = stat_arena(page, today)
    featured_arr = stat_arena(page2, today)
    success_compr = []
    status = 0
    for each2 in range(len(stat_arr)):
        for each in range(len(zulu_arr)):
            s = SequenceMatcher(None, zulu_arr[each][4], stat_arr[each2][4])
            if s.ratio() > 0.5:
                if SequenceMatcher(None, zulu_arr[each][1], stat_arr[each2][1]).ratio() > 0.6:
                    if stat_arr[each2][3].strip() != "-:-":
                        res = stat_arr[each2][3]
                    else:
                        res = zulu_arr[each][3]
                    success_compr.append([zulu_arr[each][0],zulu_arr[each][1],"%s,%s" % (zulu_arr[each][2],stat_arr[each2][2]),res,stat_arr[each2][4],zulu_arr[each][5], zulu_arr[each][6], stat_arr[each2][7]])
                    del zulu_arr[each]
                    status = 1
                    break
                else:
                    status=0
            else:
                status = 0
        if status == 1:
            stat_arr[each2] = 'remv'
            status = 0
    stat_arr_clean = [x for x in stat_arr if x!="remv"]
    combined_games = zulu_arr + success_compr
    # for allgames
    def outcome_case(outcome_text, score, case):
        if outcome_text != "no_results_yet":
            home_team_guest_team = [int(x) for x in score.split(":")]
            if case !='bts':
                if sum(home_team_guest_team) > case:
                    return "homewin"
                else:
                    return "homelose"
            else:
                if 0 not in home_team_guest_team:
                    return "homewin"
                else:
                    return "homelose"
        else:
            return "no_results_yet"

    print(combined_games)
    for each in combined_games:
        obj, created = Match.objects.update_or_create(
            name=each[4],
            defaults={
                'match_date': each[0],
                'time': each[1],
                'name': each[4]
            })
        print(obj)
        print("----------------------------------")
        print(created)
    # print("allgames done")
    # for tipGG
    # for each in stat_arr_orign:
    #     outcome = outcome_case(each[6],each[3], 'bts')
    #     if each[7]:
    #         TipGG.objects.update_or_create(
    #             teams=each[4],
    #             defaults={
    #                 'match_date': each[0],
    #                 'time': each[1],
    #                 'teams': each[4],
    #                 'tip_gg': 'G-G',
    #                 'tip_gg_odd': each[5],
    #                 'ft_results': each[3],
    #                 'outcome_text': outcome
    #             })
    #     # for Over15
    #     if each[8]:
    #         outcome = outcome_case(each[6],each[3], 1.5)
    #         Over15.objects.update_or_create(
    #             teams=each[4],
    #             defaults={
    #                 'match_date': each[0],
    #                 'time': each[1],
    #                 'teams': each[4],
    #                 'tip_ov': 'Over 1.5',
    #                 'tip_ov_odd': each[5],
    #                 'ft_results': each[3],
    #                 'outcome_text':outcome
    #             })
    #     # for Over25:
    #     if each[9]:
    #         outcome = outcome_case(each[6],each[3], 2.5)
    #         Over25.objects.update_or_create(
    #             teams=each[4],
    #             defaults={
    #                 'match_date': each[0],
    #                 'time': each[1],
    #                 'teams': each[4],
    #                 'tip_ov': 'Over 2.5',
    #                 'tip_ov_odd': each[5],
    #                 'ft_results': each[3],
    #                 'outcome_text': outcome
    #             })
    #     # for Over35
    #     if each[10]:
    #         outcome = outcome_case(each[6],each[3], 3.5)
    #         Over35.objects.update_or_create(
    #             teams=each[4],
    #             defaults={
    #                 'match_date': each[0],
    #                 'time': each[1],
    #                 'teams': each[4],
    #                 'tip_ov': 'Over 3.5',
    #                 'tip_ov_odd': each[5],
    #                 'ft_results': each[3],
    #                 'outcome_text': outcome
    #             })
    # # print("Big Thing done")
    # # for Featured Games
    # for each in featured_arr:
    #     Featured.objects.update_or_create(
    #         teams=each[4],
    #         defaults={
    #             'match_date': each[0],
    #             'time': each[1],
    #             'teams': each[4],
    #             'tip': each[2],
    #             'tip_odd': each[5],
    #             'ft_results': each[3],
    #             'outcome_text': each[6]
    #         })
    # print("Featured Games done")
