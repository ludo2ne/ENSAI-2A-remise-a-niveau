# Introduction au langage Python

Ce dossier contient des Notebooks pour apprendre les bases du langage.
Les thèmes abordés :

* [ ] Les types et variables
* [ ] Les listes
* [ ] Les dictionnaires
* [ ] Les boucles
* [ ] Les fonctions
* [ ] Introduction à la Programmation Orientée Objet (POO)
* :construction: Tests unitaires
* :construction: Exceptions

## :arrow_forward: Ressources utiles

* <https://www.data-transitionnumerique.com/anaconda-python/>
* <https://github.com/ludo2ne/projet-info-2A>
* SSPCloud
  * initiation à Python
  * Python pour la datascience
  * initiation à Spark
  * initiation au Machine Learning
  * analyse textuelle
* <https://pythonds.linogaliana.fr/rappels2a/>

## :arrow_forward: Introduction

* Python
  * 1ère version en 1991
  * gratuit
  * multiplateforme (Linux, Windows...)
  * langage interprété
    * le script python est directement exécuté
    * pas de compilation
  * langage orienté objet
  * sensible à l'indentation (généralement 4 espaces)
    * utiliser un formatage automatique (autopep8)
* Version utilisée à l'ENSAI : 3.10.4
  * dernière version : 3.11.3
* Distribution utilisée à l'ENSAI
  * CPython
  * Autre distribution populaire : Anaconda
* IDE (Integrated Development Environment) utilisé à l'ENSAI
  * Visual Studio Code
  * Autres IDE : PyCharm, Jupyter, Atom, Spyder...
* Packages
  * Informatique
    * autopep8 (formatage du code)
      * inquirerPy
      * requests
      * psycopg2-binary
      * tabulate
  * Datascience
    * NumPy
    * Pandas (manipulation et l'analyse des données, dataframe)
    * Matplotlib (graphiques 2D et 3D)

Ouvrir une invite de commandes **Git Bash**

```bash
python --version              # Python 3.10.4 
pip list                      # Packages installés
pip install <package_name>    # installer un package

# Distribution utilisée
python -c 'import platform; print(platform.python_implementation())'
```

## :arrow_forward: Installation

### :small_orange_diamond: projet Python avec VSCode

* Créer un dossier
  * à faire pour chaque nouveau projet
  * `mkdir /p/Cours2A/UE3_Remise_a_niveau/Python`
  * `cd /p/Cours2A/UE3_Remise_a_niveau/Python`
  * `mkdir src doc data`
* Ouvrir Visual Studio Code
  * File > Open Folder
  * ouvrir le dossier créé ci-dessus
* Dans `src`, créer un fichier `hello.py`
  * `print("hello")`
* Ouvrir un terminal (CTRL + ù)
  * `python src/hello.py`

---

## :arrow_forward: Utilisation des Notebooks

* Se connecter à [Jupyter](https://clust-n4.ensai.fr/)
* importer les fichiers `.ipynb`
* Autres possibilités pour utiliser des Notebooks
  * [Google Colab](https://colab.research.google.com/)
  * SSPCloud

### :small_orange_diamond: Types de cellules

Un notebook est constitué de cellules. Vous pouvez créer une nouvelle cellule en cliquant sur le bouton **`+`** dans la barre d'outils.  
Il existe deux types de cellules principaux :

* les cellules de code (où vous écrivez et exécutez du code Python)
* les cellules de texte (où vous écrivez du texte formaté en utilisant Markdown)  

Le type de cellule souhaité est modifiable dans la barre d'outils.  

### :small_orange_diamond: Commandes utiles

| Commande                   | Description                                                                       |
| -------------------------- | --------------------------------------------------------------------------------- |
| `SHIFT + ENTER`            | Exécuter une cellule et passer à la suivante.                                     |
| `CTRL + ENTER`             | Exécuter une cellule sans passer à la suivante.                                   |
| `ESC`                      | Passer en mode commande (les bordures de cellule deviennent bleues).              |
| `ENTER`                    | Passer en mode édition (vous pouvez modifier le contenu de la cellule).           |
| `A`                        | Insérer une cellule au-dessus de la cellule courante.                             |
| `B`                        | Insérer une cellule en dessous de la cellule courante.                            |
| `D + D`                    | Supprimer une cellule.                                                            |

---

## :game_die: For fun

* Chaque année en décembre, l'[AdventOfCode](https://adventofcode.com/) occupe les développeurs

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
