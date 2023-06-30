class Velo:
    """
    Classe représentant un vélo.

    Attributs:
        couleur (str): La couleur du vélo.
        vitesse (int): La vitesse actuelle du vélo.
        porte_bagage (bool): Indique si le vélo a un porte-bagage.

    Méthodes:
        __init__(couleur, porte_bagage=False): Construit un nouvel objet Velo
        __str__(): représentation en chaîne de caractères d'un objet Velo
        accelerer(acceleration): Accélère le vélo en ajoutant l'accélération à sa vitesse actuelle.
        ralentir(deceleration): Ralentit le vélo en soustrayant la décélération de sa vitesse actuelle.
        installer_porte_bagage(): Installe un porte-bagage sur le vélo en le mettant à True.
        est_arrete(): Vérifie si le vélo est complètement arrêté.

    """

    def __init__(self, couleur, porte_bagage=False):
        self.couleur = couleur
        self.vitesse = 0
        self.porte_bagage = porte_bagage

    def __str__(self):
        s = "Je suis un vélo " + self.couleur + "."
        s += " Ma vitesse est de : " + str(self.vitesse) + "."
        if self.porte_bagage:
            s += " J'ai un porte-bagages."
        return s

    def accelerer(self, acceleration):
        self.vitesse += acceleration

    def ralentir(self, deceleration):
        self.vitesse -= deceleration
        if self.vitesse < 0:
            self.vitesse = 0

    def installer_porte_bagage(self):
        self.porte_bagage = True

    def est_arrete(self):
        return self.vitesse == 0
