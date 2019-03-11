
def overall_result(result_home, result_away, tip, tipx_odd,tip1_odd,tip2_odd):
    if result_away == "post" or result_home == "post":
        win_odd = 0
        return ["postponed", win_odd]
    elif result_home == 'no_result' or result_away == 'no_result':
        win_odd = 0.0
        if tip == 'X':
            win_odd = tipx_odd.split(":")[1]
        elif tip == '1':
            win_odd = tip1_odd.split(":")[1]
        elif tip == '2':
            win_odd = tip2_odd.split(":")[1]
        elif tip == '12':
            win_odd = 0
            # get odd for double chance
        elif tip == '1X':
            win_odd = 0
            # get odd for double chance
        elif tip == 'X2':
            win_odd = 0
            # get odd for double chance
        return ['no_results_yet', win_odd]
    else:
        if tip == 'X':
            win_odd = tipx_odd.split(":")[1]
            if result_home == result_away:
                return ['drawwin', win_odd]
            else:
                return ['drawlose', win_odd]
        elif tip == '1':
            win_odd = tip1_odd.split(":")[1]
            if result_home > result_away:
                return ['homewin', win_odd]
            else:
                return ['homelose', win_odd]
        elif tip == '2':
            win_odd = tip2_odd.split(":")[1]
            if result_away > result_home:
                return ['awaywin', win_odd]
            else:
                return ['awaylose', win_odd]
        elif tip == '12':
            win_odd = 0
            if result_away != result_home:
                return ['12win', win_odd]
            else:
                return ['12lose', win_odd]
        elif tip == '1X':
            win_odd = 0
            if result_home >= result_away:
                return ['1Xwin', win_odd]
            else:
                return ['1Xlose', win_odd]
        elif tip == 'X2':
            win_odd = 0
            if result_home <= result_away:
                return ['X2win', win_odd]
            else:
                return ['X2lose', win_odd]
