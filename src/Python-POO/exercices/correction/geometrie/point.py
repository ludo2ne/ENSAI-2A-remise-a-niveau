import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance(self, autre_point):
        return math.sqrt((self.x - autre_point.x) ** 2 + (self.y - autre_point.y) ** 2)

    def __eq__(self, autre_point):
        return self.x == autre_point.x and self.y == autre_point.y


if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    print(f"p1 : {p1}")
    print(f"Distance entre p1 et p2 : {p1.distance(p2)}")
    print(f"p1 est égal à p2 : {p1 == p2}")
