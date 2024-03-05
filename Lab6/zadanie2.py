slovo  = "XochyKoLbasKy"

c=0

def slova(word):
    cc = 0
    notCC = 0
    for i in word:
        if i.isupper():
            cc += 1
        elif i.islower():
            notCC += 1   
    return cc, notCC
c, c1 = slova(slovo)        
print(c, c1)