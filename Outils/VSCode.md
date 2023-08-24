# Développer en Python avec Visual Studio Code

Visual Studio Code est un logiciel qui permet d'éditer du code et propose de nombreuses extensions.

Le but de cette fiche est de :

* vous permettre d'exécuter un programme python avec VSCode
* donner quelques astuces pour faciliter votre utilisation

## :gear: Paramétrage

* Désinstaller l'extension **Ruff**

---

## :arrow_forward: Mon 1er TP

* Ouvrir Visual Studio Code Local
* Ouvrir un terminal
  * Menu Terminal > New terminal (raccourci : CTRL + ù)
* Créer un dossier pour le TP
  * Copier cette commande : `mkdir "P:\Cours\Python\tp1"`
  * Dans le terminal, faire clic droit (Coller) puis ENTREE
  * Vérifier que les dossiers sont bien créés
    * Sinon créer les dossiers à la main
* Ouvrir un espace de travail
  * Dans VSCode : File > Open Folder
  * Sélectionner le dossier tp1 créé précédemment
  * Yes i trust...
* Créer un premier fichier python
  * Dans VSCode : File > New File (CTRL + N)
  * Ecrire dans ce fichier : `print("hello")`
  * puis File > Save (CTRL + S)
    * enregistrer dans le dossier tp1 sous le nom `bacasable.py`
* Executer le fichier
  * En haut à droite, cliquer sur l'icone en forme de triangle ▷
    * Run python file in terminal
  * Cela ouvre un terminal et exécute le fichier

---

## :arrow_forward: Le terminal python

2 modes :

* `P:\Cours\Python\tp1>`
  * pour éxecuter en totalité un fichier python
    * en cliquant sur le triangle ▷
    * en tapant la commande `python bacasable.py`
  * taper `python` en ENTREE pour passer à l'autre mode
* `>>>` pour exécuter directement du code python
  * permet d'exécuter uniquement certaines lignes du fichier
    * en cliquant sur une ligne puis SHIFT + ENTREE
    * en sélectionnant plusieurs lignes puis SHIFT + ENTREE
  * dans ce mode on peut aussi écrire directement du python dans le terminal
  * taper `quit()` ou CTRL + Z pour retourner à l'autre mode

---

## :arrow_forward: Ma 1ere fonction

Coller le code suivant et l'exécuter

```python=
def plus2(x):
    return x + 2

print(plus2(5))
```

---

## :arrow_forward: Indentation et formattage

Python est sensible à l'indentation, c'est à dire qu'un code mal indenté ne s'exécutera pas et renverra une erreur (parfois peu parlante).
Un outil utile pour écarter définitivement ce souci est le formatteur automatique

* Dans Settings :gear: (en bas à gauche)
* Dans la barre de recherche (en haut au milieu), taper `formatting`
  * Dans Python > Formatting: Autopep8 Path, taper : `autopep8`
* Dans la barre de recherche, taper `format`
  * Editor: Format On Save :arrow_right: cocher la case

Maintenant à chaque sauvegarde, le fichier sera indenté comme il faut.

:warning: Il est probable qu'à chaque nouvelle session, dans VSCode une popup dise que Autopep8 n'est pas installé

* Voulez-vous l'installer :arrow_right: Yes
* Install with pip
:

## :arrow_forward: Ma 1ere classe

* Créer un nouveau fichier nommé `voiture.py` contenant le code ci-dessous
* Exécuter le fichier
  * Python va lancer la méthode `__main__`, c'est à dire exécuter les tests unitaires

```python=
class Voiture:
    '''Définition d'une voiture

    Attributes
    ----------
    couleur : str
        couleur de la voiture
    nom : str
        nom de la voiture
    vitesse : float
        vitesse de la voiture
    '''

    def __init__(self, nom, couleur):
        '''Constructeur de l'objet
        La vitesse n'est pas un paramètre du constructeur, elle est initialisée à 0

        Parameters
        ----------
        nom : str
            nom de la voiture
        couleur : str
            couleur de la voiture

        Examples
        ---------
        >>> ma_voiture = Voiture("4L", "verte")
        >>> ma_voiture.nom == "4L"
        True
        >>> ma_voiture.couleur == "verte"
        True
        >>> ma_voiture.vitesse == 0
        True
        '''
        self.couleur = couleur
        self.nom = nom
        self.vitesse = 0

    def accelere(self, increment):
        '''Augmente la vitesse de la voiture

        Vitesse max = 130 km/h
        Augmentation max = 10 km/h

        Parameters
        ----------
        increment : float
            accélération

        Examples
        ---------
        >>> ma_voiture = Voiture('4L', 'verte')
        >>> ma_voiture.accelere(15)
        >>> ma_voiture.vitesse == 10
        True
        '''
        # si l increment est negatif rien ne se passe
        if increment < 0:
            return
        if increment > 10:
            increment = 10
        self.vitesse = min(130, self.vitesse + increment)

    def freine(self, decrement):
        '''Diminue la vitesse de la voiture

        Vitesse min = 0 km/h

        Parameters
        ----------
        decrement : float
            décélération

        Examples
        ---------
        >>> ma_voiture = Voiture('4L', 'verte')
        >>> ma_voiture.accelere(10)
        >>> ma_voiture.freine(8)
        >>> ma_voiture.vitesse == 2
        True
        '''
        if decrement < 0:
            return
        self.vitesse = max(0, self.vitesse - max(0, decrement))

    def est_arretee(self):
        '''La voiture est-elle à l'arrêt ?

        Returns
        -------
        bool
            True si elle est à 0 km/h

        Examples
        ---------
        >>> ma_voiture = Voiture('4L', 'verte')
        >>> ma_voiture.est_arretee()
        True
        >>> ma_voiture.accelere(5)
        >>> ma_voiture.est_arretee()
        False
        '''
        return self.vitesse == 0

    def __str__(self):
        '''Convertit la voiture en chaîne de caractères

        Examples
        ---------
        >>> ma_voiture = Voiture('4L', 'verte')
        >>> print(ma_voiture)
        voiture 4L de couleur verte à l'arrêt.
        >>> ma_voiture.accelere(2)
        >>> print(ma_voiture)
        voiture 4L de couleur verte roule à 2 km/h.
        '''
        v = 'roule à ' + str(self.vitesse) + ' km/h'
        if self.est_arretee():
            v = "à l'arrêt"

        return "voiture {} de couleur {} {}.".format(self.nom, self.couleur, v)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

```

Entre les `'''` se trouvent :

* de la documentation pour expliquer comment fonctionne la classe
* des tests unitaires (sous le tag Examples)
  * ils permettent de vérifier si la méthode est correcte

---

## :arrow_forward: Python, VSCode et les packages

Imaginez que votre code est organisé de la manière ci-dessous

```
├───tp1
│   └───code
│   │   ├───vehicule
│   │   │   ├───velo.py
│   │   │   └───trottinette.py
│   │   ├───animal
│   │   │   ├───girafe.py
│   │   │   └───ane.py
```

Si dans la classe ==Girafe==, vous voulez créer un objet de la classe ==Velo==, vous pouvez par exemple faire ceci dans le code de girafe.py :

* import de la classe Velo
* puis création d'un objet ==Velo==

```python=
from vehicule.velo import Velo

class Girafe:
    def __init__(self, nom, nom_moyen_transport):
        self.nom = nom
        vehicule = None
        if nom_moyen_transport == "velo":
            vehicule = Velo()
        self.moyen_transport = vehicule
```

:rotating_light: Cependant, il se peut que que VSCode et/ou le compilateur python n'apprécient pas ce genre d'imports et que vous rencontriez des erreurs du type **le module velo n'existe pas**

Comme solution de contournement, vous pouvez :

* en reprenant l'arborescence ci-dessus,
* dans le dossier code créer un dossier ==.vscode==
* dans ce dossier .vscode, créer le fichier settings.json qui contient ceci :

```json
{
    "python.analysis.extraPaths": [
        "./*"
    ],
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "${workspaceFolder}/src",
    },
    "terminal.integrated.env.linux": {
        "PYTHONPATH": "${workspaceFolder}/src",
    },
    "python.languageServer": "Jedi"
}
```

* puis fermer et redémarrer VSCode
* File > Open Folder > `C:/.../tp1/code`

## :arrow_forward: Afficher les variables d'environnement

```bash=
printenv
echo $PYTHONPATH
echo $HOME
```
