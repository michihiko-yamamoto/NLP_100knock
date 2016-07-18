def create_bigram(str):
    bigram = []
    for i in range(1,len(str)):
        bigram.append(str[i-1]+str[i])
    return bigram

x = "paraparaparadise"
y = "paragraph"

x_bigram = set(create_bigram(x))
y_bigram = set(create_bigram(y))

print x_bigram.union(y_bigram)
print x_bigram.difference(y_bigram)
print x_bigram.intersection(y_bigram)

print "se" in x_bigram
print "se" in y_bigram
