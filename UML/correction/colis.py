"""
Module des courrrier
"""
import doctest
from courrier import Courrier


class Colis(Courrier):
    """Définition d'un colis

    Examples
    --------
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
        return "Volume : {} litres".format(self.volume)

    def calcul_affranchissement(self):
        """Calcule l'affranchissement

        Returns
        --------
        float
           prix du timbre

        Examples
        --------
        >>> c1 = Colis(10,"","","",8)
        >>> c1.calcul_affranchissement()
        12
        """
        tarif = self.volume / 4 + self.poids * 0.001
        if self.expedition_rapide:
            tarif *= 2
        return tarif


if __name__ == "__main__":
    doctest.testmod(verbose=True)
