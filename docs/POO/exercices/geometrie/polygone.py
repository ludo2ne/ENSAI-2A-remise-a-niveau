from abc import ABC, abstractmethod


class Polygone(ABC):
    def __init__(self, points):
        """points : list[Points]"""
        self.points = points

    @abstractmethod
    def aire(self):
        pass

    @abstractmethod
    def perimetre(self):
        pass
