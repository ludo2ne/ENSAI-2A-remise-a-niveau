class Domino:
    '''
    Classe représentant un domino
    Attributs :
        extr_A : le coté gauche
        extr_B : le coté droit
    Méthodes
        retourner() : inverse les 2 extrémités
        accepte_apres(autreDomino) : vérifie si l'extrémité B
            du domino courant a la même valeur que l'extrémité A
            de l'autre domino
    '''
    def __init__(self, a, b):
        self.extr_A = a
        self.extr_B = b

    def __str__(self):
        return "[{} , {}]".format(self.extr_A, self.extr_B)

    def retourner(self):
        tmp = self.extr_A
        self.extr_A = self.extr_B
        self.extr_B = tmp
        return self

    def accepte_apres(self, autre_domino) -> bool:
        return self.extr_B == autre_domino.extr_A
