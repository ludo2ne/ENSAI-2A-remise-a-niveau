"""
Module des courrrier
"""
import doctest
from abc import abstractmethod


class Courrier:
    """Définition d'un article

    Examples
    --------
    """

    def __init__(self, poids, expedition_rapide, adresse_destination):
        """Constructeur

        Parameters
        ----------
        poids : float
            Poids en kilogramme
        expedition_rapide : bool
            True si mode d'expédition rapide
        adresse_destination : str
            Adresse de destination
        """
        self.poids = poids
        self.expedition_rapide = expedition_rapide
        self.adresse_destination = adresse_destination

    @abstractmethod
    def calcul_affranchissement(self):
        pass

    def __str__(self):
        """Affichage d'un courrier"""
        return """
            Colis :
            Adresse destination : {}
            Poids : {} grammes
            Mode : {}
            {}
            Prix du timbre : {}€""".format(
            self.adresse_destination,
            self.poids,
            self.expedition_rapide,
            self.complement_str(),
            self.calcul_affranchissement(),
        )

    @abstractmethod
    def complement_str(self):
        pass
