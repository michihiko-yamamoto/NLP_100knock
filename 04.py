str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = str.replace('.','').split()
ind = (1,5,6,7,8,9,15,16,19)
dict = {}
for i,s in enumerate(words):
    if i+1 in ind:
        dict[s[0]] = i+1
    else:
        dict[s[:2]] = i+1
print dict
    
