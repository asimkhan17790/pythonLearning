class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return Point((self.x+p.x), (self.y+p.y))

    def print_point(self):
        print(f"({self.x}, {self.y})")

    def __add__(self, p):  # Built in methods that can be overriden.
        return Point((self.x+p.x), (self.y+p.y))


p1 = Point(3, 2)
p2 = Point(6, 3)

p = p1.sum(p2)  # Returns new point which is sum of p1 and p2
p.print_point()

p3 = p1 + p2  # Operator overloading: we overloaded + operator by overriding the __add__ method
p3.print_point()

# Lets use + tp add the points
