---
title: 2A Remise à niveau
tags: Pro
---

[TOC]


# Liens utiles

* [GitHub](https://github.com/HealerMikado/Cours-Ensai-Informatique/tree/master/2A/remise%20niveau%20info)


# :arrow_forward: Contenu

* 21h
* SQL 3h
    * connaissent souvent un peu, attention quand même aux produits cartésiens
* Python et Algo 6h
    * niveau : bof
* POO 9h
    * ne connaissent généralement pas du tout
* UML 3h
    * ne connaissent généralement pas du tout
    * diag de cas d'utilisation et de classe
    * memento UML disponibles à la bibliothèque




---

# :arrow_forward: Introduction

## Programme

* SQL
* Python
    * Git
* POO
* UML

Parler un peu de : 
* R
* HackMd
* LateX

## Quelques tips

* view.ensai.fr
* CTRL + ALT + F12
* Impression

### Créer son arborescence de travail

#### avec git bash

variables ENV (set)
* HOME
* HOMEPATH
* USERNAME
* USERPROFILE


#### via l'explorer




---

# :arrow_forward: SQL

* [ ] ACID
* [ ] 

## Intro

SQL (Structured Query Language) est un langage de programmation utilisé pour gérer et manipuler des bases de données relationnelles.

* BDD (Base de données) = ensemble de tableaux 
    * BDD relationnelle : utilise des relations pour établir des liens entre les tables
        * exemple

Il permet d'effectuer les opérations suivantes sur les données d'une base de données (CRUD) : 
* créer : INSERT
* lire : SELECT
* modifier : UPDATE
* supprimer : DELETE

Table : 
* clé primaire (PK)
* clés étrangères (FK)


### Actions sur les colonnes

Créer une Table
```sql
CREATE TABLE personne (
    id               INT         PRIMARY KEY,
    nom              VARCHAR(30) NOT NULL,
    prenom           VARCHAR(40),
    date_naissance   DATE,
    adresse          TEXT
);
```

| id | nom    | prenom | date_naissance | adresse |
|----|--------|--------|----------------|---------|

Insérer des données dans cette Table

```sql
INSERT INTO personnes (id, nom, prenom, dnais, adresse)
VALUES
    (1, 'Dupont', 'Jean', '1990-05-15', 'Paris'),
    (2, 'Martin', 'Emma', '1985-09-22', 'Lyon'),
    (3, 'Leroy', 'Paul', '1995-03-10', 'Lille');
```

| id | nom    | prenom | date_naissance | adresse |
|----|--------|--------|----------------|---------|
| 1  | Gatore | Ali    | 1990-05-15     | Paris   |
| 2  | Dure   | Laure  | 1985-09-22     | Lyon    |
| 3  | Erateur| Maud   | 1995-03-10     | Lille   |


Renommer la colonne **date_naissance**

```sql
ALTER TABLE personnes
RENAME COLUMN date_naissance TO dnais;
```

| id | nom    | prenom | dnais      | adresse |
|----|--------|--------|------------|---------|
| 1  | Gatore | Ali    | 1990-05-15 | Paris   |
| 2  | Dure   | Laure  | 1985-09-22 | Lyon    |
| 3  | Erateur| Maud   | 1995-03-10 | Lille   |



Ajouter un attribut booléen **joue_aux_echecs**

```sql
ALTER TABLE personnes
ADD joue_aux_echecs BOOLEAN;
```

| id | nom    | prenom | dnais      | adresse | echecs |
|----|--------|--------|------------|---------|--------|
| 1  | Gatore | Ali    | 1990-05-15 | Paris   | true   |
| 2  | Dure   | Laure  | 1985-09-22 | Lyon    | false  |
| 3  | Erateur| Maud   | 1995-03-10 | Lille   | true   |


Supprimer la colonne **adresse**
```sql
ALTER TABLE personnes
DROP COLUMN adresse;
```

| id | nom    | prenom | dnais      | echecs |
|----|--------|--------|------------|--------|
| 1  | Gatore | Ali    | 1990-05-15 | true   |
| 2  | Dure   | Laure  | 1985-09-22 | false  |
| 3  | Erateur| Maud   | 1995-03-10 | true   |



Supprimer la table **personnes**
```sql
DROP TABLE personnes;
```



### Actions sur les lignes

| id | prenom | nom    | date_naissance | adresse |
|----|--------|--------|----------------|---------|

Insérer des lignes

```sql
INSERT INTO personnes (id, nom, prenom, date_naissance, adresse)
VALUES
    (1, 'Ali', 'Gatore', '1990-05-15', 'Paris'),
    (2, 'Laure', 'Dure', '1985-09-22', 'Lyon'),
    (3, 'Maud', 'Erateur', '1995-03-10', 'Lille');

```

| id | prenom | nom    | date_naissance | adresse |
|----|--------|--------|----------------|---------|
| 1  | Ali    | Gatore | 1990-05-15     | Paris   |
| 2  | Laure  | Dure   | 1985-09-22     | Lyon    |
| 3  | Maud   | Erateur| 1995-03-10     | Lille   |


**Sélectionner** des lignes avec des restrictions

```sql
SELECT *
  FROM personnes
 WHERE adresse LIKE 'L%'
   AND prenom = 'Laure';
```

| id | prenom | nom    | date_naissance | adresse |
|----|--------|--------|----------------|---------|
| 2  | Laure  | Dure   | 1985-09-22     | Lyon    |

Jointure

> [color=red] TODO

**Mettre à jour**

```sql
UPDATE personnes
SET adresse = 'Rennes'
WHERE id = 2;
```

| id | prenom | nom    | date_naissance | adresse |
|----|--------|--------|----------------|---------|
| 1  | Ali    | Gatore | 1990-05-15     | Paris   |
| 2  | Laure  | Dure   | 1985-09-22     | Rennes  |
| 3  | Maud   | Erateur| 1995-03-10     | Lille   |


**Supprimer** des lignes

```sql
DELETE FROM personnes
WHERE prenom = 'Ali';
```

| id | prenom | nom    | date_naissance | adresse |
|----|--------|--------|----------------|---------|
| 2  | Laure  | Dure   | 1985-09-22     | Rennes  |
| 3  | Maud   | Erateur| 1995-03-10     | Lille   |



Principaux SGBD : 
* PostgreSQL
* Oracle Database 
* MySQL
* Microsoft SQL Server

## Outils

### DBeaver

> [color=red] TODO

> * Fenêtre > Preference
>     * Formatage SQL
>         * Casse des mots clefs : UPPER
>         * [ ] Insert spaces for tabs
>     * Templates
>         * sf > Modifier
>             * Schéma = ==SELECT * FROM jdr.==
>     * Métadonnées
>         * Décocher "Ouvrir une connexion séparée pour la lecture des métadonnées"
>     * Editeur SQL
>         * Décocher "Ouvrir une connexion séparée pour chaque éditeur"
> 
> 
> Pour créer une connexion vers la base de données ENSAI sur la VM : 
> * cliquer sur icone ==Nouvelle connexion== en haut à gauche sous fichier
> * PostgreSQL puis suivant
>     * Host : sgbd-eleves.domensai.ecole
>     * Port : 5432
>     * Database : idxxxx
>     * Nom d'utilisateur : idxxxx
>     * Mot de passe : idxxxx
> * cliquer sur l'icone ==SQL== 
>     * coller les scripts ci-dessous (à la racine du projet)
>     * à chaque fois cliquer sur la 3e icone orange ==Executer le script SQL==
>         * init_db.sql
>         * pop_db.sql


### Interface pgAdmin

Une autre solution pour éxécuter des requêtes SQL est de passer par l'interface pgAdmin

> [color=red] TODO


## Exercices

### Base de données ==echecs==

> [color=red] TODO : fichier echecs en bdd

1. Lister les joueurs
2. Créer un nouveau joueur
3. Supprimer le joueur **Sam Gratte**
4. Lister les joueurs qui sont arbitres
5. Lister les joueurs qui sont arbitres, ainsi que leur grade d'arbitre
6. Créer une table pour codifier la colonne **vainqueur** de la table **parties**
7. Créer une vue
8. Ajouter une contrainte sur la table **joueur** pour que le **elo** soit entre 1000 et 3000


# Python

https://www.data-transitionnumerique.com/anaconda-python/
https://github.com/ludo2ne/projet-info-2A

## Introduction

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