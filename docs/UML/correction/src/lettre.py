"""
Module des courrrier
"""
from courrier import Courrier


class Lettre(Courrier):
    """Définition d'une lettre"""

    def __init__(self, poids, expedition_rapide, adresse_destination, format):
        """
        Parameters
        ----------
        format : str
            Format de la lettre (A3 ou A4)
        """
        super().__init__(poids, expedition_rapide, adresse_destination)
        self.format = format

    def complement_str(self) -> str:
        return "Format : {}".format(self.format)

    def calcul_affranchissement(self) -> float:
        """Calcule l'affranchissement

        Returns
        --------
        float
           prix du timbre
        """
        tarif = 0
        if self.format == "A4":
            tarif = 2.5 + self.poids * 0.001
        else:
            tarif = 3.5 + self.poids * 0.001

        if self.expedition_rapide:
            tarif *= 2

        return tarif
