# SQL

## :arrow_forward: Programme

* [ ] introduction
* [ ] installation
* [ ] exercices

### Notions à aborder

* [ ] ACID

---

## :arrow_forward: Introduction

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

---

## :arrow_forward: Actions sur les colonnes

### :small_orange_diamond: Créer une Table

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

> La table est créée mais vide

---

### :small_orange_diamond: Insérer des données dans cette Table

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

---

### :small_orange_diamond: Renommer la colonne `date_naissance`

```sql
ALTER TABLE personnes
RENAME COLUMN date_naissance TO dnais;
```

| id | nom    | prenom | dnais      | adresse |
|----|--------|--------|------------|---------|
| 1  | Gatore | Ali    | 1990-05-15 | Paris   |
| 2  | Dure   | Laure  | 1985-09-22 | Lyon    |
| 3  | Erateur| Maud   | 1995-03-10 | Lille   |

---

### :small_orange_diamond: Ajouter un attribut booléen `joue_aux_echecs`

```sql
ALTER TABLE personnes
ADD joue_aux_echecs BOOLEAN;
```

| id | nom    | prenom | dnais      | adresse | echecs |
|----|--------|--------|------------|---------|--------|
| 1  | Gatore | Ali    | 1990-05-15 | Paris   | true   |
| 2  | Dure   | Laure  | 1985-09-22 | Lyon    | false  |
| 3  | Erateur| Maud   | 1995-03-10 | Lille   | true   |

---

### :small_orange_diamond: Supprimer la colonne `adresse`

```sql
ALTER TABLE personnes
DROP COLUMN adresse;
```

| id | nom    | prenom | dnais      | echecs |
|----|--------|--------|------------|--------|
| 1  | Gatore | Ali    | 1990-05-15 | true   |
| 2  | Dure   | Laure  | 1985-09-22 | false  |
| 3  | Erateur| Maud   | 1995-03-10 | true   |

---

### :small_orange_diamond: Supprimer la table `personnes`

```sql
DROP TABLE personnes;
```

---

## :arrow_forward: Actions sur les lignes

| id | prenom | nom    | date_naissance | adresse |
|----|--------|--------|----------------|---------|

### :small_orange_diamond: Insérer des lignes

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

---

### :small_orange_diamond: Sélectionner des lignes avec des restrictions

```sql
SELECT *
  FROM personnes
 WHERE adresse LIKE 'L%'
   AND prenom = 'Laure';
```

| id | prenom | nom    | date_naissance | adresse |
|----|--------|--------|----------------|---------|
| 2  | Laure  | Dure   | 1985-09-22     | Lyon    |

---

### :small_orange_diamond: Jointures entre tables

> * [ ] :construction:

---

### :small_orange_diamond: Mettre à jour des lignes

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

---

### :small_orange_diamond: Supprimer des lignes

```sql
DELETE FROM personnes
WHERE prenom = 'Ali';
```

| id | prenom | nom    | date_naissance | adresse |
|----|--------|--------|----------------|---------|
| 2  | Laure  | Dure   | 1985-09-22     | Rennes  |
| 3  | Maud   | Erateur| 1995-03-10     | Lille   |

---

## :arrow_forward: Principaux SGBD

* PostgreSQL
* Oracle Database
* MySQL
* Microsoft SQL Server

---

## :arrow_forward: Outils

### :small_orange_diamond: DBeaver

> * Fenêtre > Preference
>   * Formatage SQL
>     * Casse des mots clefs : UPPER
>     * [ ] Insert spaces for tabs
>   * Templates
>     * sf > Modifier
>       * Schéma = ==SELECT * FROM jdr.==
>   * Métadonnées
>     * Décocher "Ouvrir une connexion séparée pour la lecture des métadonnées"
>   * Editeur SQL
>     * Décocher "Ouvrir une connexion séparée pour chaque éditeur"
>
> Pour créer une connexion vers la base de données ENSAI sur la VM :
>
> * cliquer sur icone ==Nouvelle connexion== en haut à gauche sous fichier
> * PostgreSQL puis suivant
>   * Host : sgbd-eleves.domensai.ecole
>   * Port : 5432
>   * Database : idxxxx
>   * Nom d'utilisateur : idxxxx
>   * Mot de passe : idxxxx
> * cliquer sur l'icone ==SQL==
>   * coller les scripts ci-dessous (à la racine du projet)
>   * à chaque fois cliquer sur la 3e icone orange ==Executer le script SQL==
>     * init_db.sql
>     * pop_db.sql

### :small_orange_diamond: Interface pgAdmin

Une autre solution pour éxécuter des requêtes SQL est de passer par l'interface pgAdmin

> * [ ] :construction:

---

## :arrow_forward: Exercices

### Base de données `echecs`

> * [ ] :construction: TODO : fichier echecs en bdd

1. Lister les joueurs
2. Créer un nouveau joueur
3. Supprimer le joueur **Sam Gratte**
4. Lister les joueurs qui sont arbitres
5. Lister les joueurs qui sont arbitres, ainsi que leur grade d'arbitre
6. Créer une table pour codifier la colonne **vainqueur** de la table **parties**
7. Créer une vue
8. Ajouter une contrainte sur la table **joueur** pour que le **elo** soit entre 1000 et 3000
