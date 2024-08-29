import random as rnd

from domino import Domino


class Jeu:
    """
    Classe pour représenter un Jeu de Dominos
    Attributs :
        dominos_poses : liste des Dominos joués
        dominos_joueur : liste des Dominos dans la main du joueur
        dominos_restants : liste de tous les autres Dominos
    """

    def __init__(self):
        self.dominos_restants = self.generer_tous()
        self.dominos_joueur = []
        self.dominos_poses = []

    def affiche_dominos(self, liste_dominos) -> None:
        """
        Affiche la liste de Domino en paramètre
        """
        print(" - ".join([str(d) for d in liste_dominos]))

    def generer_tous(self) -> list[Domino]:
        """
        Générer tous les dominos
        i.e. toutes les combinaisons unique de couple entre 0 et 6
        """
        liste_dominos = []
        for i in range(0, 7):
            for j in range(i, 7):
                d = Domino(i, j)
                liste_dominos.append(d)
        return liste_dominos
        # equivalent à : return [Domino(i, j) for i in range(0, 7) for j in range(i, 7)]

    def piocher(self) -> Domino:
        """
        Pioche un Domino dans la liste des dominos_restants
        """
        index = rnd.randint(0, len(self.dominos_restants) - 1)
        domino_pioche = self.dominos_restants.pop(index)
        return domino_pioche

    def poser_premier_domino(self) -> None:
        """
        Pioche un 1er Domino dans dominos_restants et le place dans dominos_poses
        """
        self.dominos_poses.append(self.piocher())

    def distribuer_au_joueur(self) -> None:
        """
        Distribue 6 Domino au joueur (au début de la partie)
        Pioche 6 Domino dans dominos_restants et les met dans dominos_joueur
        """
        for i in range(6):
            domino = self.piocher()
            self.dominos_joueur.append(domino)

    def dominos_posables(self) -> list[Domino]:
        """
        Liste des Dominos que le joueur a le droit de poser
        """
        d_posables = []
        for d in self.dominos_joueur:
            if self.dominos_poses[-1].accepte_apres(d) or self.dominos_poses[-1].accepte_apres(
                d.retourner()
            ):
                d_posables.append(d)
        return d_posables

    def poser_domino(self, domino) -> None:
        """
        Le joueur pose le Domino en paramètre
        Retire le Domino de dominos_joueur et l'ajoute dans dominos_poses
        """
        if self.dominos_poses[-1].accepte_apres(domino):
            self.dominos_poses.append(domino)
        elif self.dominos_poses[-1].accepte_apres(domino.retourner()):
            self.dominos_poses.append(domino)
        else:
            print("\n\n" + "*" * 20 + " WARNING " + "*" * 20)
            print("Le Domino suivant n'est pas posable : " + str(domino))
            print("Il est remis dans votre liste de Dominos")
            print("*" * 49 + "\n\n")
            self.dominos_joueur.append(domino)

    def choix_joueur(self) -> Domino:
        """
        Retourne le Domino choisi par le joueur
        """
        domino = None
        while True:
            i = input(
                "Indiquez le numéro du domino que vous souhaitez jouer (de 0 à "
                + str(len(self.dominos_joueur) - 1)
                + ") --- ou p pour piocher --- ou q pour quitter : "
            )

            if i == "q":
                break
            elif i == "p":
                self.dominos_joueur.append(self.piocher())
                self.afficher_jeu()
            else:
                i = int(i)
                if 0 <= i < len(self.dominos_joueur):
                    domino = self.dominos_joueur.pop(i)
                    break
                print("Numéro invalide")

        return domino

    def afficher_jeu(self) -> None:
        """
        Affiche les Dominos du joueur et ceux posés
        """
        print("\n" + "-" * 100)
        print("Dominos posés :")
        j.affiche_dominos(j.dominos_poses)

        print("-" * 50)
        print("Dominos du joueur :")
        j.affiche_dominos(j.dominos_joueur)
        # print("Dominos posables : ", end='')
        # j.affiche_dominos(j.dominos_posables())
        print("-" * 100)


if __name__ == "__main__":
    """
    Pour lancer le jeu
    """

    j = Jeu()
    j.distribuer_au_joueur()
    j.poser_premier_domino()

    while True:
        j.afficher_jeu()

        domino_a_jouer = j.choix_joueur()
        if domino_a_jouer is None:
            print("Merci d'avoir joué")
            break
        else:
            j.poser_domino(domino_a_jouer)
