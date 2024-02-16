import math
print("Write measurements:")
def Area(sides, length):
    A = (sides * pow(length, 2)) / (4 * math.tan(math.pi/sides))
    return A

sides=int(input())
length =int(input())

area = Area(sides, length)
print("Area is:")
print(math.floor(area))