from math import pi

class Shape:
    def area(self): pass

#Shape Rectangle
class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

#Shape Square
class Square(Rectangle):
    def __init__(self, s):
        super().__init__(s, s)

#Shape Circle
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r ** 2

#Shape Triangle
class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return 0.5 * self.b * self.h


r = Rectangle(20, 10)
s = Square(25)
c = Circle(60)
t = Triangle(60, 75)

print("Rectangle Area:", r.area())
print("Square Area:", s.area())
print("Circle Area:", c.area())
print("Triangle Area:", t.area())
