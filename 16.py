# -*- coding: utf-8 -*-

import sys
param = sys.argv
templist = []
for l in open("hightemp.txt","r"):
    templist.append(l.strip())

n = len(templist)/(int(param[1]))
d = len(templist)%n
for i,l in enumerate(templist):
    if (i+1)%(n+1) == 0 and d != 0:
        print ""
    elif (i+1)%n == 0:
        print ""
        d -= 1
    print l

