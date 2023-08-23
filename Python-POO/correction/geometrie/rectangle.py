from quadrilatere import Quadrilatere
from point import Point


class Rectangle(Quadrilatere):

    def __init__(self, points):
        if len(points) == 4 and self.verif_rectangle(points):
            super().__init__(points)
        else:
            print("Vous n'avez pas le bon nombre de points")

    def verif_rectangle(self, points):
        res = True

        # TODO

        return res


if __name__ == "__main__":
    p1, p2, p3, p4 = Point(0, 0), Point(3, 0), Point(3, 4), Point(0, 4)
    t = Rectangle([p1, p2, p3, p4])
    print(t.perimetre())
    print(t.aire())
