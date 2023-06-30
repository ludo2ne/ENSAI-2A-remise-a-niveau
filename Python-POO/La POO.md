
# La Programmation Orientée Objet (POO)

La POO est un paradigme de programmation qui permet d'organiser et de structurer le code en utilisant des objets. Les objets sont des entités qui regroupent des données (attributs) et des actions (méthodes) qui leur sont associées. La POO repose sur plusieurs principes fondamentaux :

* **Encapsulation** : L'encapsulation consiste à regrouper les données et les méthodes qui les manipulent au sein d'un même objet. Cela permet de cacher les détails d'implémentation et de fournir une interface cohérente pour interagir avec l'objet
* **Héritage** : L'héritage permet de créer de nouvelles classes à partir de classes existantes, en héritant de leurs attributs et méthodes. Cela favorise la réutilisation du code et la création d'une hiérarchie de classes
* **Polymorphisme** : Le polymorphisme permet à des objets de classes différentes de répondre de manière différente à une même action. Cela permet de manipuler des objets de différentes classes de manière uniforme, en utilisant des interfaces communes

La POO permet :

* d'organiser le code de manière plus structurée
* de favoriser la réutilisation et la maintenance du code
* de modéliser les concepts du domaine d'application de manière naturelle

Elle est largement utilisée dans de nombreux langages de programmation, dont Python, pour développer des applications complexes et évolutives.

---

## :arrow_forward: Organisation du code

Dans la suite, nous allons organsier notre code de manière logique dans différents modules.

> **module** : Les modules d’un programme Python sont ses fichiers sources.

> **paquet** : Un paquet (package en anglais) est un ensemble de modules dans le même dossier.

### :bulb: bonne pratique

A la racine de votre projet, créez les 3 dossiers suivants :

* **src** : pour stocker votre code source
* **data** : pour vos fichiers de données
* **doc** : pour votre documentation

```
.
├── data
│   └── temperatures.csv
├── doc
│   ├── suivi.md
│   └── rapport.tex
└── src
    ├── __main__.py
    ├── package1
    │   ├── __init__.py
    │   ├── module1.py
    │   ├── module2.py
    └── package2
        ├── __init__.py
        ├── module3.py
        └── subpackage21
            ├── __init__.py
            ├── module4.py
            ├── module5.py
```

Remarques importantes :

* le fichier `__main__.py` contient le code à exécuter quand le pacakge est exécuté
* les fichiers `__init__.py` sont des fichiers qu'il faut créer dans chaque module pour pouvoir les utiliser (c'est comme ça...)

Voici un exemple plus concret :

```
.
└── src
    ├── __main__.py
    ├── vehicules
    │   ├── __init__.py
    │   ├── deux_roues.py
    │   ├── velo.py
    │   └── trottinette.py
    └── humain
        ├── __init__.py
        ├── personne.py
        └── etudiant.py
```

## :arrow_forward: Exercices

### Exercice 1 - Points

voir ipoo - tp4

Créer une classe `Point`

```python
class Point:
def __init__(self, x, y):
self.px = x self.py = y
def decaler(self, dx, dy): return Point(self.px + dx, self.py + dy)
def __str__(self): return "({}, {})".format(self.px, self.py)
```

### Exercice 2 - Domino

voir ipoo tp3

### Exercice 3 - Polygones

voir ipoo tp5
