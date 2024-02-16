def sqrTT(start, stop):
    while start < stop:
        yield start**2
        start +=1

start = int(input())
stop = int(input())+1

sq = sqrTT(start, stop)
list = []

for square in sqrTT(start, stop):
    for x in range (start, stop):
        if square == x**2:
            list.append(square)
   
print(', '.join(map(str, list)))


