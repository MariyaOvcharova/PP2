def ToZero(n):
    for i in range(0, n):
        while n!=-1:
            yield n
            n -=1

n = int(input())
ee = list(ToZero(n))

print(', '.join(map(str, ee)))