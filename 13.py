# -*- conding:utf-8 -*-
col1 = []
for l in open("col1_py.txt","r"):
    col1.append(l.strip())

col2 = []
for l in open("col2_py.txt","r"):
    col2.append(l.strip())

for i in range(len(col1)):
    print col1[i]+'\t'+col2[i]

