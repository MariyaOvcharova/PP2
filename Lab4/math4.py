print("Write measurements:")

def Area(h, a):
    A=a*h
    return A

h=int(input())
a=int(input())


area = Area(h, a)
area = float(area)
print("Area of parallelogram is:")
print(area)