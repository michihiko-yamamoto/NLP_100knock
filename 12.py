# -*- coding: utf-8 -*-
templist = []
fout1 = open("col1_py.txt","w") 
fout2 = open("col2_py.txt","w") 
for l in open("hightemp.txt","r"):
    templist.append(l.split('\t'))
for s in templist:
    fout1.write(s[0]+'\n')
    fout2.write(s[1]+'\n')
