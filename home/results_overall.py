
def overall_result(result_home, result_away, tip, tipx_odd,tip1_odd,tip2_odd):
    if result_away == "post" or result_home == "post":
        win_odd = 0
        return ["postponed", win_odd]
    elif result_home == 'no_result' or result_away == 'no_result':
        win_odd = 0.0
        if tip == 'X':
            win_odd = tipx_odd
        elif tip == '1':
            win_odd = tip1_odd
        elif tip == '2':
            win_odd = tip2_odd
        elif tip == '12':
            win_odd = 0
            # get odd for double chance
        elif tip == '1X':
            win_odd = 0
            # get odd for double chance
        elif tip == 'X2':
            win_odd = 0
            # get odd for double chance
        return ['waiting', win_odd]
    else:
        if tip == 'X':
            win_odd = tipx_odd
            if result_home == result_away:
                return ['won', win_odd]
            else:
                return ['lost', win_odd]
        elif tip == '1':
            win_odd = tip1_odd
            if result_home > result_away:
                return ['won', win_odd]
            else:
                return ['lost', win_odd]
        elif tip == '2':
            win_odd = tip2_odd
            if result_away > result_home:
                return ['won', win_odd]
            else:
                return ['lost', win_odd]
        elif tip == '12':
            win_odd = 0
            if result_away != result_home:
                return ['won', win_odd]
            else:
                return ['lost', win_odd]
        elif tip == '1X':
            win_odd = 0
            if result_home >= result_away:
                return ['won', win_odd]
            else:
                return ['lost', win_odd]
        elif tip == 'X2':
            win_odd = 0
            if result_home <= result_away:
                return ['won', win_odd]
            else:
                return ['lost', win_odd]
