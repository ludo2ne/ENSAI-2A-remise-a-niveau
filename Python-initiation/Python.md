---
title: 2A Python
tags: Pro
---

# :construction: TODO

* https://www.data-transitionnumerique.com/anaconda-python/
* https://github.com/ludo2ne/projet-info-2A
* SSPCloud
    * initiation à Python
    * Python pour la datascience
    * initiation à Spark
    * initiation au Machine Learning
    * analyse textuelle
* https://pythonds.linogaliana.fr/rappels2a/
* [ ] Introduction, présentation
* [ ] Installation
* [ ] Premiers programmes




# Introduction

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

# Installation

## projet Python avec VSCode

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


## Notebook

* Cluster Jupyter ENSAI : https://clust-n4.ensai.fr/
* Google Colab : https://colab.research.google.com/


---

# Premiers pas avec le langage

* Types et variables
    * Nombres, Chaînes de caractères, Booléens
    * [x] cours
    * [ ] exercices
* Conteneurs
    * Liste, Dictionnaire
    * [x] cours
    * [ ] exercices
* Boucles
    * ifelse, for, while
    * [ ] cours
    * [ ] exercices
* Fonctions
    * [ ] cours
    * [ ] exercices
* Tests unitaires
* Exceptions


# :game_die: For fun

* https://adventofcode.com/







<style>
   /* headers level 1 # */
    h1{
        color: darkblue;
        font-family: "Calibri";
        background-color: darkseagreen;
        padding-left: 10px;
    }
    h2{
        color: darkblue;        
    }
    h3{
        color: darkred;        
    }
    h4{
        color: purple;        
    }
</style>