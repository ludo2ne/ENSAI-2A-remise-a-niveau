# Développer en Python avec Visual Studio Code

Visual Studio Code est un logiciel qui permet d'éditer du code et propose de nombreuses extensions.

Le but de cette fiche est de :

* vous permettre d'exécuter un programme python avec VSCode
* donner quelques astuces pour faciliter votre utilisation

## :gear: Paramétrage

### :small_orange_diamond: Extensions

De très nombreuses extensions permettent d'améliorer votre utilisation de VSCode.
Sur la version utilisées à l'ENSAI, vous pouvez trouver déjà installé :

* Black Formatter
* Flake8
* isort
* Python Test Explorer
* ...
* [ ] Désactiver l'extension **Ruff** (elle fait doublon avec **Flake8**)

### :small_orange_diamond: Formatage et Linting

* Un **formateur** est un outil qui va mettre en forme votre code pour que ce soit joli et lisible
* un **linter** est un outil qui va vous avertir si votre code n'est pas joli
  * ex : ligne trop longue, espace manquant ou en trop...

Les extensions Black Formatter et Flake8 sont respectivement un formateur et un linter

### :small_orange_diamond: Settings

Vous pouvez préciser le paramètrage à plusieurs niveaux :

* au niveau de l'application VSCode
* au niveau d'un dépôt

Le fichier `.vscode/settings.json` contient du paramètrage qui va s'appliquer à tous les fichiers du dépôt.

Ce fichier contient par exemple les propriétés ci-dessous :

```json
    "flake8.args": [
        "--max-line-length=120"
    ],
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
        "editor.insertSpaces": true,
        "editor.tabSize": 4
    },
```

---

## :arrow_forward: Première utilisation

> Nous allons créer un dépôt local avec Git, puis ouvrir ce dépôt avec VSCode

* Ouvrir Visual Studio Code
* Ouvrir un terminal
  * Menu Terminal > New terminal (raccourci : CTRL + ù)
* Créer un dossier pour le TP
  * Copier cette commande : `mkdir -p /p/Cours2A/UE3_Remise_a_niveau`
  * Dans le terminal, faire clic droit (Coller) puis ENTREE
  * Vérifier que les dossiers sont bien créés, sinon créer les dossiers à la main
* Cloner le dépôt
  * Se postionner dans le dossier créé : `cd /p/Cours2A/UE3_Remise_a_niveau`
  * `git clone https://github.com/ludo2ne/ENSAI-2A-remise-a-niveau.git`
* Ouvrir un espace de travail
  * Dans VSCode : File > Open Folder
  * Sélectionner le dossier `P:/Cours2A/UE3_Remise_a_niveau/ENSAI-2A-remise-a-niveau` créé précédemment
  * Yes i trust...
* Ouvrir, puis exécuter un fichier Python
  * Ouvrir le fichier `Python-POO/src/__main__.py`
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

---

<style>
    h1{
        color: darkblue;
        font-family: "Calibri";
        font-weight: bold;
        background-color: seagreen;
        padding-left: 10px;
    }
    h2{
        color: darkblue;
        background-color: mediumseagreen;
        margin-right: 10%;
        padding-left: 10px;
    }
    h3{
        color: darkblue;
        background-color: darkseagreen;
        margin-right: 20%;
        padding-left: 10px;
    }
    h4{
        color: darkblue;
        background-color: lightseagreen;
        margin-right: 30%;
        padding-left: 10px;
    }
    h5{
        color: darkblue;
        background-color: aquamarine;
        margin-right: 40%;
        padding-left: 10px;
    }
</style>
