import re
import csv
from texas_holdem_hashtable import suit_dep, not_suit_dep


with open('poker_lookup_table.py', 'w') as file:
    file.write("not_suit_dep = { \n")
    a=[]
    for key in not_suit_dep.keys():
        b=sorted(key)
        b="".join(b)
        a.append(b)


    for k, h in zip(a, not_suit_dep.keys()):
        file.write("'%s':'%s', \n" % (k, not_suit_dep[h]))
    file.write("}")

    file.write("\n\n\nsuit_dep = { \n")
    a=[]
    for key in suit_dep.keys():
        b=sorted(key)
        b="".join(b)
        a.append(b)


    for k, h in zip(a, suit_dep.keys()):
        file.write("'%s':'%s', \n" % (k, suit_dep[h]))
    file.write("}")

