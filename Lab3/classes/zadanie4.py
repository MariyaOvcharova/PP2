class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"{self.x}", f"{self.y}")

    def move(self, x1, y1):
        self.x = x1
        self.y = y1

    def dist(self, point):
        distt = ((self.x-point.x)**2+(self.y-point.y)**2)**0.5
        return distt
    
    
pointtt = Point(5, 7)
pointtt.show()

pointt = Point(0, 0)
    
pointtt.move(3,2)
pointtt.show()
pointt.show()

print(pointtt.dist(pointt))


