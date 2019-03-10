#! this is where huge comparison goes b4 data is insterted into database
from home.statArena import stat_arena
from home.zulubet import ZuluGames
from difflib import SequenceMatcher

def boiler(url, today):
    cust_arr = ZuluGames(url, today).zulu_procedure()
    cust2 = stat_arena()
    print("Games One length: %s\nGames two length: %s" % (len(cust_arr), len(cust2)))
    count = 0
    success_compr = []
    status = 0
    for each2 in range(len(cust2)):
        print("Outer Loop remaining %d" % len(cust2))
        print("each2 in outer loop %s" % each2)
        for each in range(len(cust_arr)):
            print("each in inner loop %s" % each)
            s = SequenceMatcher(None, cust_arr[each][2], cust2[each2][3])
            if s.ratio() > 0.5:
                if SequenceMatcher(None, cust_arr[each][1], cust2[each2][0]).ratio() > 0.6:
                    count+=1
                    ##                    print("%s / %s  Efficiency %s" % (cust_arr[each][2], cust2[each2][3], SequenceMatcher(None, cust_arr[each][2], cust2[each2][3]).ratio()))
                    success_compr.append(cust2[each2])
                    print("index for each %d" % each)
                    del cust_arr[each]
                    ##                    cust_arr[each][2]+" looks like \n
                    print("index for each2 %d" % each2)
                    status = 1
                    break
                else:
                    status=0
            else:
                status = 0
        # print("Counter Level %d" % count)
        # print("status %d" % status)
        if status == 1:
            # print("index for each2 outer %d" % each2)
            cust2[each2] = 'remv'
            status = 0

        # print("Inner Loop remaining %d" % len(cust_arr))
    print("Games that could be compared are %d out of %d" % (count, len(cust2)))
    cust2_clean = [x for x in cust2 if x!="remv"]
    print("Games one length unmatched: %s\nGames two length unmatched: %s" %(len(cust_arr), len(cust2_clean)))
    print(cust_arr+cust2_clean+cust2)
