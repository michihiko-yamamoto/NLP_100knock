# -*- coding: utf-8 -*-

preflist = []
for l in open("hightemp.txt","r"):
    preflist.append(l.strip().split()[0])
preflist = list(set(preflist))
for s in preflist:
    print s
