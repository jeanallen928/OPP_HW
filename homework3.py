class Shape():
    def get_area():
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * (self.radius**2)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


won = Circle(1)
nemo = Rectangle(2, 3)

print(won.radius)

print(won.get_area())
print(nemo.get_area())
