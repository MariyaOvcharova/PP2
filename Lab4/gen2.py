def EvEn(n):
    for i in range(1, n+1):
        if i%2==0:
            yield i
            i +=1

n = int(input())
ee = list(EvEn(n))

print(', '.join(map(str, ee)))