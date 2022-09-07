# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

class Rectangle:
    """Models a Rectangle"""

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

class Circle:
    """Models a Circle"""

    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return (self.radius * self.radius) * 3.14159
    
    def circumference(self):
        return (self.radius * 2) * 3.14159

rect1 = Rectangle(10, 5)
circle1 = Circle(7)

print(Rectangle.area(rect1))
print(Rectangle.perimeter(rect1))

print(Circle.area(circle1))
print(Circle.circumference(circle1))