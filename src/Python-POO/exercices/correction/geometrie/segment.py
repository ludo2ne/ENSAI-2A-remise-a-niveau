from point import Point
from polygone import Polygone


class Segment(Polygone):
    def __init__(self, points):
        if len(points) == 2:
            super().__init__(points)
        else:
            print("Vous n'avez pas le bon nombre de points")

    def aire(self) -> float:
        return 0

    def perimetre(self) -> float:
        p1 = self.points[0]
        p2 = self.points[1]
        return p1.distance(p2)


if __name__ == "__main__":
    p1, p2 = Point(0, 0), Point(3, 4)
    s = Segment([p1, p2])
    print(s.perimetre())
    s2 = Segment([p1])
