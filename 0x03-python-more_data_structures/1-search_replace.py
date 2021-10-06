#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nlist = my_list.copy()
    for x in nlist:
        try:
            x = nlist.index(search)
        except:
            return nlist
        nlist[x] = replace
    return nlist
