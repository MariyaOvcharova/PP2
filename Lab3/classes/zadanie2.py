class Shape:
    def __init__(self):
        pass 
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, lenght):
        self.length = lenght
    
    def area(self):
        return self.length**2

lenght = int(input())

obj = Square(lenght)

print(obj.area())