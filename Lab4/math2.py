print("Write measurements:")

def Area(h, b1, b2):
    A=(b1+b2)*h / 2
    return A

h=int(input())
b1=int(input())
b2=int(input())

area = Area(h, b1, b2)
print("Area of trapezoid is:")
print(area)