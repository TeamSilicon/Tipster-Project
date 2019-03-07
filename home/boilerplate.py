#! this is where huge comparison goes b4 data is insterted into database
from home.statArena import stat_arena
from home.zulubet import ZuluGames
from difflib import SequenceMatcher

def boiler(url, today):
    cust_arr = ZuluGames(url, today).zulu_procedure()
    cust2 = stat_arena()
    count = 0
    failed_comp = []
    success_compr = []
    for each, each2 in zip(cust_arr, cust2):
        s = SequenceMatcher(None, each[2], each2[3])
        print("zulu %s Arena %s  Efficiency %s" % (each[1], each2[0], SequenceMatcher(None, each[1], each2[0]).ratio()))
        if s.ratio() > 0.6:
            if SequenceMatcher(None, each[1], each2[0]).ratio() > 0.6:
                count+=1
                success_compr.append(each[2]+" looks like \n" +each2[3])
        else:
            failed_comp.append(each2[3])
    print("Games that could be compared are %d out of %d" % (count, len(cust2)))
    print("\n".join(success_compr))
    print("Couldn't be compared games\n")
    print("\n".join(failed_comp))
