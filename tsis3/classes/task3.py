class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, l, w):
        Shape.__init__(self)
        self.length = l
        self.width = w
    def area(self):
        return self.length*self.width
Rctg = Rectangle(12, 10)
print(Rctg.area())