import math

from polygone import Polygone
from point import Point


class Triangle(Polygone):

    def __init__(self, points):
        if len(points) == 3:
            super().__init__(points)
        else:
            print("Vous n'avez pas le bon nombre de points")

    def aire(self):
        a = self.points[0].distance(self.points[1])
        b = self.points[0].distance(self.points[2])
        c = self.points[1].distance(self.points[2])
        p = (a + b + c) / 2
        return math.sqrt(p*(p-a)*(p-b)*(p-c))

    def perimetre(self):
        s = self.points[0].distance(self.points[1])
        s += self.points[0].distance(self.points[2])
        s += self.points[1].distance(self.points[2])
        return s


if __name__ == "__main__":
    p1, p2, p3 = Point(0, 0), Point(3, 4), Point(0, 4)
    t = Triangle([p1, p2, p3])
    print(t.perimetre())
    print(t.aire())
