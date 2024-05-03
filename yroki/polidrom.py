def isPolidrome(num):
    temp = str(num)
    return temp == temp[::-1]

def myRange(start, stop):
    while start < stop:
        yield start
        start +=1

print(isPolidrome(121), isPolidrome(122))

