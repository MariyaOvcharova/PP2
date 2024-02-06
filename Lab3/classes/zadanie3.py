class Shape:
    def __init__(self):
        pass 
    
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.length = lenght
        self.width = width  
    
    def area(self):
        return self.length*self.width

lenght = int(input())
width = int(input())

obj = Rectangle(lenght, width)

print(obj.area())