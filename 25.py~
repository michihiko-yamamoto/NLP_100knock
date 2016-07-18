#-*-: coding: utf-8 -*-
import json
import re
coudict = {}
for l in open("jawiki-country.json","r"):
    tmpdict = json.loads(l)
    coudict[tmpdict['title'].encode('utf-8')] = tmpdict['text'].encode('utf-8')
pattern = r"(?<=\{\{基礎情報 国).*?\n\}\}\n"
match = re.search(pattern,coudict['イギリス'],re.DOTALL)
fund_info = match.group().replace("\n}}\n","")
for cate in  fund_info.replace('\n',"").split("|"):
        print cate

