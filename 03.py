str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = str.replace(',','').replace('.','').split()
for s in words:
    print len(s)

