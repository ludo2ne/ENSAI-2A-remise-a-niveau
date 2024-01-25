"""
Module des courrriers
"""
from courrier import Courrier


class Colis(Courrier):
    """Définition d'un colis
    """

    def __init__(self, poids, expedition_rapide, adresse_destination, volume):
        """
        Parameters
        ----------
        volume : float
            Volume en litres
        """
        super().__init__(poids, expedition_rapide, adresse_destination)
        self.volume = volume

    def complement_str(self) -> str:
        return f"Volume : {self.volume} litres"

    def calcul_affranchissement(self):
        """Calcule l'affranchissement

        Returns
        --------
        float
           prix du timbre
        """
        tarif = self.volume / 4 + self.poids * 0.001
        if self.expedition_rapide:
            tarif *= 2
        return tarif

