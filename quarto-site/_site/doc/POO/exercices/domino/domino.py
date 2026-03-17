class Domino:
    """
    Classe représentant un domino
    Attributs :
        extr_A : int
            le coté gauche
        extr_B : int
            le coté droit
    Méthodes
        retourner() : inverse les 2 extrémités
        accepte_apres(autreDomino) : vérifie si l'extrémité B
            du domino courant a la même valeur que l'extrémité A
            de l'autre domino
    """

    def __init__(self, a, b):
        self.extr_A = a
        self.extr_B = b

    def __str__(self) -> str:
        return f"[{self.extr_A} , {self.extr_B}]"

    def retourner(self) -> "Domino":
        """Inverse l'extrémité A et l'extrémité B et retourne le domino inversé."""
        self.extr_A, self.extr_B = self.extr_B, self.extr_A
        return self

    def accepte_apres(self, autre_domino) -> bool:
        """
        True si le côté B du domino courant est égal au côté A
        du domino que l'on souhaite poser après.
        """
        return self.extr_B == autre_domino.extr_A
