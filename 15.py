# -*- coding: utf-8 -*-
import sys
param = sys.argv
templist = []
for l in open("hightemp.txt","r"):
    templist.append(l.strip())

for i in range(len(templist)):
    if len(templist) - i <= int(param[1]):
        print templist[i]

    
