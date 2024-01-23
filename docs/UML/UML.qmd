# UML

UML (Unified Modeling Language) est un langage de modélisation graphique largement utilisé dans le domaine de l'ingénierie logicielle. Il fournit un ensemble de notations et de diagrammes standardisés pour représenter visuellement différents aspects d'un système logiciel.

L'objectif principal d'UML est de faciliter la communication, la compréhension et la documentation des systèmes logiciels complexes. Il permet aux concepteurs, développeurs et parties prenantes de collaborer efficacement en utilisant des diagrammes compréhensibles et normalisés.

Les 3 principaux diagrammes :

* **Diagramme de cas d'utilisation** (Use Case Diagram) : Il représente les fonctionnalités fournies par un système logiciel du point de vue des utilisateurs (acteurs). Il montre les interactions entre les acteurs et le système.
* **Diagramme de classes** (Class Diagram) : Il représente la structure statique d'un système logiciel en montrant les classes du système, leurs attributs, leurs méthodes et les relations entre les classes. Il permet de modéliser les concepts, les relations et les dépendances entre les classes.
* **Diagramme d'activité** (Activity Diagram) : Il représente le flux de contrôle à l'intérieur d'un système logiciel ou d'un processus métier. Il montre les étapes, les décisions, les branchements et les flux de données.
* ...

> :bulb: Memento UML disponibles à la bibliothèque

## :arrow_forward: Exercice

### Exercice 1 : Courrier

Un Courrier peut être de 2 types : Lettre ou Colis.

Une Lettre est caractérisée par :

* poids (en grammes)
* mode d'expédition (Rapide ou Normal)
* adresse de destination
* format (A3 ou A4)

Un Colis est caractérisé par :

* poids (en grammes)
* mode d'expédition (Rapide ou Normal)
* adresse de destination
* volume (en litres)

Chaque Courrier dispose des méthodes suivantes :

* `__init__()` : un constructeur
* `__str__()` : une méthode qui retourne une chaine décrivant le Courrier
* `calcul_affranchissement()`
  * pour une Lettre : tarif_base + poids * 0.001
    * avec tarif_base = 2€50 pour le format A4 et 3€50 pour le A3
  * pour un colis : volume / 4 + poids * 0.001
  * en mode d'expédition rapide, les montants ci-dessus sont doublés

Questions :

* [ ] Définir le diagramme de classe
* [ ] Coder ces classes en Python

Exemple de résultat attendu

```python
>>> l1 = Lettre("Bordeaux", 80, "normal", "A4")
>>> print(l1)
Lettre : 
    Adresse destination : Bordeaux
    Poids : 80 grammes
    Mode : normal
    Format : A4
    Prix du timbre : 2.58 €
>>> c1 = Colis("Rennes", 3500, "rapide", 2.25)
>>> print(c1)
Colis : 
    Adresse destination : Rennes 
    Poids : 3500 grammes 
    Mode : rapide 
    Volume : 2.25 litres 
    Prix du timbre : 8.12 €
```



<style>
    body{
        text-align: justify;
    }
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
