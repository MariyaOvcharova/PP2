import  itertools

def Str(str):
    return list(itertools.permutations(str))

strr = Str(input())

print(strr)

def Revverse(str1):
    str2 = str1.split()
    reversestr1 = str2[::-1]
    # print(reversestr1)
    str5 = " "
    str5 = str5.join(reversestr1)
    print(str5)

strr4 = Revverse(input())

