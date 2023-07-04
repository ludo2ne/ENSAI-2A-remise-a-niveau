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

:bulb: le `ran.` correspond au schéma de la remise à niveau dans lequel nous rangerons toutes les tables

```sql
-- Création de la table personne (ceci est un commentaire)
CREATE TABLE ran.personnes (
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
INSERT INTO ran.personnes (id, nom, prenom, dnais, adresse)
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
ALTER TABLE ran.personnes
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
ALTER TABLE ran.personnes
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
ALTER TABLE ran.personnes
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
DROP TABLE ran.personnes;
```

```
> ERREUR: la relation « ran.personnes » n'existe pas
```

---

## :arrow_forward: Actions sur les lignes

| id | prenom | nom    | date_naissance | adresse |
|----|--------|--------|----------------|---------|

### :small_orange_diamond: Insérer des lignes

```sql
INSERT INTO ran.personnes (id, nom, prenom, date_naissance, adresse)
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
  FROM ran.personnes
 WHERE adresse LIKE 'L%'
   AND prenom = 'Laure';
```

| id | prenom | nom    | date_naissance | adresse |
|----|--------|--------|----------------|---------|
| 2  | Laure  | Dure   | 1985-09-22     | Lyon    |

---

### :small_orange_diamond: Jointures entre tables

> Table `commande`

| id | produit | quantite | id_client | prix_unitaire |
|----|---------|----------|-----------|---------------|
| 1  | livre   | 1        | 2         | 3             |

```sql
SELECT p.prenom,
       c.produit,
       c.quantite
  FROM ran.personnes p
  JOIN ran.commandes c ON p.id = c.id_client
 WHERE prenom = 'Laure';
```

> :bulb: il est possible d'utiliser le mot clé `USING` à la place de `ON` si les 2 colonnes permettant la jointure ont le même nom.  
> exemple : si dans la table `personnes` nous avons `id_client` au lieu de `id`, la requête ci-dessous peut-être modifiée en :

```sql
SELECT p.prenom,
       c.produit,
       c.quantite
  FROM ran.personnes p
  JOIN ran.commandes c USING(id_client) -- <--
 WHERE prenom = 'Laure';
```

---

### :small_orange_diamond: Jointures externes

> Que se passe t'il si nous exécutons la requête ci-dessous et qu'Ali n'a passé aucune commande ?

```sql
SELECT p.prenom,
       c.produit,
       c.quantite
  FROM ran.personnes p
  JOIN ran.commandes c ON p.id = c.id_client
```

Pour afficher toutes les personnes, même celles qui n'ont pas réalisé de commande, nous allons utiliser les **jointures externees** : `LEFT JOIN` ou `RIGHT JOIN`

```sql
SELECT p.prenom,
       c.produit,
       c.quantite
  FROM ran.personnes p
  LEFT JOIN ran.commandes c ON p.id = c.id_client
```

---

### :small_orange_diamond: Mettre à jour des lignes

```sql
UPDATE ran.personnes
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
DELETE FROM ran.personnes
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

## :arrow_forward: Premières manipulations

> voir fichier `DBeaver.md` pour le paramétrage

### :small_orange_diamond: Les schémas

Par défaut toutes les tables que nous allons créer iraient dans le schéma public.  
:bulb: pour une meilleure organisation, nous allons classer nos tables dans différents schémas :

* `ran` : schéma utilisé pour la remise à niveau
* `ci` : schéma utilisé en complément d'informatique
* `projet` : schéma du projet info 2A

```sql
CREATE schema ran;
CREATE schema ci;
CREATE schema projet;
```

### :small_orange_diamond: Mots clés utiles

#### :large_blue_circle: LIKE

> Utilisé dans une clause WHERE pour effectuer des recherches de motif dans une colonne

```sql
-- toutes les personnes ayant un prénom contenant "au"
SELECT 
  FROM ran.personnes
 WHERE prenom LIKE '%au%';
```

#### :large_blue_circle: GROUP BY

> Utilisé pour regrouper les résultats en fonction d'une ou plusieurs colonnes et permettre l'utilisation de fonctions d'agrégation telles que COUNT, SUM, AVG

```sql
-- toutes les personnes ayant un prénom contenant "au"
SELECT adresse,
       COUNT(1)
  FROM ran.personnes
 GROUP BY adresse;
```

#### :large_blue_circle: HAVING

> Utilisé après la clause GROUP BY pour filtrer les résultats en fonction d'une condition après le GROUP BY.  
> :warning: ne pas confondre avec `WHERE` qui s'appliquerait avant le `GROUP BY`

```sql
-- toutes les personnes ayant un prénom contenant "au"
SELECT adresse,
       COUNT(1)
  FROM ran.personnes
 GROUP BY adresse
HAVING COUNT(1) >= 5;
```

#### :large_blue_circle: ORDER BY

```sql
SELECT *
  FROM ran.personnes
 ORDER BY adresse DESC
```

#### :large_blue_circle: AS

> Permet de renommer une colonne dans l'affichage

```sql
SELECT adresse AS Ville
  FROM ran.personnes
```

### :small_orange_diamond: Quelques possibilités d'utilisation sans table

```sql
SELECT CURRENT_DATE;
SELECT 1+2;
SELECT 1 > 2;
SELECT 'Salut';
```

---

## :arrow_forward: Exercices

### Base de données `echecs`

Copiez le contenu du fichier `echecs.sql` dans DBeaver, puis exécuter le script

* [ ] Listez tous les joueurs
* [ ] Listez tous les joueurs ordonnés par elo descroissant
* [ ] Listez tous les joueurs ayant un elo inférieur ou égal à 2000
* [ ] Listez tous les joueurs ayant un elo inférieur ou égal à 2000 et dont le prénom contient un `e` (majuscule ou minuscule) :bulb: *tip : voir méthode `UPPER`*
* [ ] Créez la joueuse "Martine Dupont, elo : 1999, Arbitre Elite"
* [ ] Supprimez le joueur de pseudo `marc78`
* [ ] Listez les joueurs qui sont arbitres :bulb: *voir `IS NOT NULL`*
* [ ] Ajoutez à la table joueur la colonne de type booléen `est_arbitre`
* [ ] Remplissez cette nouvelle colonne pour tous les joueurs
* [ ] Listez les joueurs (nom, prénom) qui sont arbitres, ainsi que leur grade d'arbitre
* [ ] Listez **tous** les joueurs (nom, prénom) ainsi que leur grade d'arbitre s'ils le sont
* [ ] Comptez le nombre de joueurs qui sont arbitre
* [ ] Comptez le nombre d'arbitres par grade
* [ ] Comptez le nombre d'arbitres par grade et n'afficher que si la moyenne elo des arbitres du grade est supérieure à 2000
