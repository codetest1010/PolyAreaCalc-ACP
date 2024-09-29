class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides

class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__(3)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Square(Polygon):
    def __init__(self, side):
        super().__init__(4)
        self.side = side

    def area(self):
        return self.side ** 2

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)
        self.length = length
        self.width = width

    def ares(self):
        return self.length * self.width

if __name__ == "__main__":
    triangle = Triangle(5, 8)
    print("Area of triangle:", triangle.area())

    square = Square(6)
    print("Area of square:", square.area())

    rectangle = Rectangle(4, 7)
    print("Rectangle area:", rectangle.ares())