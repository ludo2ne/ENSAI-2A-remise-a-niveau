import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def distance(self, autre_point):
        """Distance à un autre point"""
        return math.sqrt((self.x - autre_point.x) ** 2 + (self.y - autre_point.y) ** 2)

    def __eq__(self, autre_point):
        """Test d'égalité avec un autre Point"""
        return self.x == autre_point.x and self.y == autre_point.y

    def r(self):
        """Rayon dans les coordonnées polaires."""
        return math.sqrt(self.x**2 + self.y**2)

    def t(self):
        """Angle dans les coordonnées polaires."""
        return math.atan2(self.y, self.x)

    def homothetie(self, k):
        """Homothétie de centre (0, 0) et de rapport k."""
        self.x *= k
        self.y *= k

    def translation(self, dx, dy):
        """Translation de vecteur (dx, dy)"""
        self.x += dx
        self.y += dy

    def rotation(self, a):
        """Rotation de centre (0, 0) et d'angle a (en radians)."""
        new_x = self.x * math.cos(a) - self.y * math.sin(a)
        new_y = self.x * math.sin(a) + self.y * math.cos(a)
        self.x = new_x
        self.y = new_y


if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    print(p1)
    print(p1.distance(p2))
    print(p1 == p2)
