def sqrT(n):
    for i in range(0, n):
        yield (i+1)**2
        i +=1

n = int(input())
sqq = list(sqrT(n))

print(', '.join(map(str, sqq)))