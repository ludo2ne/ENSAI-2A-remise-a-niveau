from point import Point
from quadrilatere import Quadrilatere
from triangle import Triangle


class Rectangle(Quadrilatere):
    def __init__(self, points):
        if len(points) != 4:
            print("Vous n'avez pas le bon nombre de points")
        elif not self.verif_rectangle(points):
            print("Pas un rectangle")
        else:
            super().__init__(points)

    def verif_rectangle(self, points) -> bool:
        res = True

        # verif cotes opposes de meme longueur
        if points[0].distance(points[1]) != points[2].distance(points[3]):
            res = False
        if points[1].distance(points[2]) != points[0].distance(points[3]):
            res = False

        # verif que 3 points forment un triangle rectangle
        t = Triangle([points[0], points[1], points[2]])
        if not t.est_rectangle():
            res = False

        return res


if __name__ == "__main__":
    p1, p2, p3, p4 = Point(0, 0), Point(3, 0), Point(3, 4), Point(0, 4)
    t = Rectangle([p1, p2, p3, p4])
    print(t.perimetre())
    print(t.aire())
