#-*-: coding: utf-8 -*-
import json
import re
coudict = {}
for l in open("jawiki-country.json","r"):
    tmpdict = json.loads(l)
    coudict[tmpdict['title'].encode('utf-8')] = tmpdict['text'].encode('utf-8')
pattern = r"File:.*?\|"
for match in re.finditer(pattern,coudict['イギリス']):
    print match.group().replace("File:","").replace("|","")

