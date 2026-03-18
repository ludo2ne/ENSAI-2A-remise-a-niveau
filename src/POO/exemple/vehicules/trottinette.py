from vehicules.deux_roues import DeuxRoues


class Trottinette(DeuxRoues):
    """
    Classe représentant une trottinette (hérite de la classe DeuxRoues)

    Attributs:
        couleur (str): La couleur du trottinette
        motorise (bool): Indique si la trottinette est motorisée
        vitesse (int): La vitesse actuelle de la trottinette

    Méthodes:
        __init__(couleur, porte_bagage=False): Construit un nouvel objet
        __str__(): représentation en chaîne de caractères de l'objet
        accelerer(): Accélère la trottinette
        ralentir(): Ralentit la trottinette

    """
    # ------------------------------------------------------------
    # Constructeur
    # ------------------------------------------------------------

    def __init__(self, couleur, motorise):
        # -------------------
        # Attributs
        # -------------------
        super().__init__(couleur, motorise)    # Appel du constructeur de la classe mère

    # ------------------------------------------------------------
    # Méthode spéciale pour afficher
    # ------------------------------------------------------------

    def __str__(self):
        s = "Je suis une trottinette "
        if self.motorise:
            s += "électrique "
        s += self.couleur + "."
        s += " Ma vitesse est de : " + str(self.vitesse) + "."
        return s

    # ------------------------------------------------------------
    # Méthodes
    # ------------------------------------------------------------

    def accelerer(self):
        if self.motorise:
            self.vitesse += 10
        else:
            self.vitesse += 5

    def ralentir(self):
        self.vitesse -= 10
        if self.vitesse < 0:
            self.vitesse = 0
