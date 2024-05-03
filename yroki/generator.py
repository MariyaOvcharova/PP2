a = range(5)
x = list(a)
print(x)


def myRange(start, stop):
    while start < stop:
        yield start
        start +=1

print(list(myRange(1, 20)))

nums = list(myRange(1, 20))
print(', '.join(map(str, nums)))


def myRange(start, stop):
    while start < stop:
        yield str(start)
        start +=1


nums = list(myRange(1, 20))
print(', '.join(nums))

def sqrTT(start, stop):
    while start < stop:
        yield start**2
        start +=1

sq = list(sqrTT(1, 20))
print(', '.join(map(str, sq)))
