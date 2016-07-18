# -*- coding: utf-8 -*-
import sys
param = sys.argv
for i,l in enumerate(open("hightemp.txt","r")):
    print l.strip()
    if i+1 >= int(param[1]):
        break

