#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    z = []
    for x in my_list:
        if x < 0:
            if x % -2 == 0:
                z.append(True)
            else:
                z.append(False)
        else:
            if x % 2 == 0:
                z.append(True)
            else:
                z.append(False)
    return z
