def filterr(n):
    if n<=1:
        return False
    
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
    
listt = [1, 2, 3, 4, 5, 6, 7, 8, 9]

primme = list(filter(lambda z: filterr(z), listt))

print(primme)
        