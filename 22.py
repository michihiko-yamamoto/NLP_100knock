# -*-: coding: utf-8 -*-
import json
coudict = {}
for l in open("jawiki-country.json","r"):
    tmpdict = json.loads(l)
    coudict[tmpdict['title'].encode('utf-8')] = tmpdict['text'].encode('utf-8')
for s in coudict['イギリス'].split('\n'):
    if "[Category:" in s:
        print s.replace("[[Category:","").replace("]]","")

