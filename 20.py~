# -*- coding: utf-8 -*-
import json
coudict = {}
for l in open("jawiki-country.json","r"):
    tmpdict = json.loads(l)
    coudict[tmpdict['title'].encode('utf-8')] = tmpdict['text'].encode('utf-8')
print coudict['イギリス']
