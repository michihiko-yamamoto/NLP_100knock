def cipher(str):
    ans = ""
    for s in str:
        if s.islower():
            ans = ans + chr(219 - ord(s))
        else:
            ans = ans + s
    return ans

w =  cipher("testtest")
print w,cipher(w)

