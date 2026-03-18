from vehicules.deux_roues import DeuxRoues


class Velo(DeuxRoues):
    """
    Classe représentant un vélo (hérite de la classe DeuxRoues)

    Attributs:
        couleur (str): La couleur du vélo.
        motorise (bool): Indique si le vélo est motorisé
        vitesse (int): La vitesse actuelle du vélo.
        porte_bagage (bool): Indique si le vélo a un porte-bagage.

    Méthodes:
        __init__(couleur, porte_bagage=False): Construit un nouvel objet Velo
        __str__(): représentation en chaîne de caractères d'un objet Velo
        accelerer(): Accélère le vélo.
        ralentir(): Ralentit le vélo.
        installer_porte_bagage(): Installe un porte-bagage sur le vélo.

    """
    # ------------------------------------------------------------
    # Constructeur
    # ------------------------------------------------------------

    def __init__(self, couleur, motorise, porte_bagage=False):
        # -------------------
        # Attributs
        # -------------------
        super().__init__(couleur, motorise)    # Appel du constructeur de la classe mère
        self.porte_bagage = porte_bagage

    # ------------------------------------------------------------
    # Méthode spéciale pour afficher
    # ------------------------------------------------------------

    def __str__(self):
        s = "Je suis un vélo "
        if self.motorise:
            s += "électrique "
        s += self.couleur + "."
        s += " Ma vitesse est de : " + str(self.vitesse) + "."
        if self.porte_bagage:
            s += " J'ai un porte-bagages."
        return s

    # ------------------------------------------------------------
    # Méthodes
    # ------------------------------------------------------------

    def accelerer(self):
        if self.motorise:
            self.vitesse += 15
        else:
            self.vitesse += 10

    def ralentir(self):
        self.vitesse -= 10
        if self.vitesse < 0:
            self.vitesse = 0

    def installer_porte_bagage(self):
        self.porte_bagage = True
