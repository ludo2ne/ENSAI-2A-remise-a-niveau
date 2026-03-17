from point import Point
from polygone import Polygone
from triangle import Triangle


class Quadrilatere(Polygone):

    def __init__(self, points):
        if len(points) == 4:
            super().__init__(points)
        else:
            print("Vous n'avez pas le bon nombre de points")

    def aire(self):
        p0 = self.points[0]
        p1 = self.points[1]
        p2 = self.points[2]
        p3 = self.points[3]

        return Triangle([p0, p1, p2]).aire() + Triangle([p0, p2, p3]).aire()

    def perimetre(self):
        s = self.points[0].distance(self.points[1])
        s += self.points[1].distance(self.points[2])
        s += self.points[2].distance(self.points[3])
        s += self.points[3].distance(self.points[0])
        return s


if __name__ == "__main__":
    p1, p2, p3, p4 = Point(0, 0), Point(3, 4), Point(0, 4), Point(-3, 2)
    t = Quadrilatere([p1, p2, p3, p4])
    print(t.perimetre())
    print(t.aire())
