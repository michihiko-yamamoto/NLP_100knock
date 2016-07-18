# -*-: coding: utf-8 -*-
import json
import re
coudict = {}
for l in open("jawiki-country.json","r"):
    tmpdict = json.loads(l)
    coudict[tmpdict['title'].encode('utf-8')] = tmpdict['text'].encode('utf-8')
for s in coudict['イギリス'].split('\n'):
    if '==' in s:
        n = s.count('=')/2 -1
        print "%s %d" % (s.replace('=','').strip(),n)

