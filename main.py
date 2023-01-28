class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b

from rectangle import Rectangle, Square

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
print(rect_1.get_area())
print(rect_2.get_area())
