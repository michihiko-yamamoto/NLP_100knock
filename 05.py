str = "I am an NLPer"
words = str.split()

word_bigram = []
for i in range(1,len(words)):
    word_bigram.append(words[i-1] + ' ' + words[i])
print word_bigram

char_bigram = []
for s in words:
    for i in range(1,len(s)):
        char_bigram.append(s[i-1]+s[i])
print char_bigram
