import random
def randomize_word(s):
    s = list(s)
    random.shuffle(s)
    return "".join(s)

sent = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

words = sent.split()
ans = ""
for s in words:
    if len(s) >= 5:
        s = randomize_word(s)
    ans = ans + " " + s
print ans
