from abc import ABC, abstractmethod


class DeuxRoues(ABC):
    """
    Classe abstraite représentant un deux-roues.

    Attributes:
        couleur (str): La couleur du deux-roues.
        vitesse (float): la vitesse en km/h, initialisée à 0
        motorise (bool): vrai si le deux-roues est motorisé
    """

    def __init__(self, couleur, motorise):
        self.couleur = couleur
        self.vitesse = 0
        self.motorise = motorise

    @abstractmethod
    def accelerer(self):
        pass

    @abstractmethod
    def ralentir(self):
        pass

    def est_arrete(self):
        return self.vitesse == 0
