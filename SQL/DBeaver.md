# Outils de gestion des SGBD

## :arrow_forward: DBeaver

> DBeaver est un outil de gestion de base de données multiplateforme et open source. Il offre une interface graphique conviviale pour se connecter, gérer et requêter différentes bases de données, notamment MySQL, PostgreSQL, Oracle, SQL Server, SQLite, et bien d'autres encore.

### :small_orange_diamond: Configuration

* Menu Fenêtre > Preference
  * Formatage SQL
    * Casse des mots clefs : `UPPER`
    * [x] Insert spaces for tabs
    * Appliquer
  * Templates
    * Enlever les modèles existants
    * Importer le fichier `templates_dbeaver.xml`
  * Metadonnées
    * Décocher "Ouvrir une connexion séparée pour la lecture des étadonnées"
  * Editeur SQL
    * Décocher "Ouvrir une connexion séparée pour chaque éditeur"

---

### :small_orange_diamond: Créer la connexion

Pour créer une connexion vers la base de données ENSAI sur la VM :

* cliquer sur icone `Nouvelle connexion` en haut à gauche sous fichier
* Sélectionner `PostgreSQL` puis suivant
  * Host : `sgbd-eleves.domensai.ecole`
  * Port : `5432`
  * Database : `idxxxx`
  * Nom d'utilisateur : `idxxxx`
  * Mot de passe : `idxxxx`
  * `Test de connexion`
  * `Terminer`

---

### :small_orange_diamond: Exécuter du SQL

* cliquer sur l'icone **SQL**
* pour exécuter :
  * CTRL + ENTREE
  * le petit triangle orange
  * le triangle orange à l'intérieur d'un parachemin pour exécuter toutes les requêtes

---

## :arrow_forward: Interface pgAdmin

Une autre solution pour éxécuter des requêtes SQL est de passer par l'interface pgAdmin

> * [ ] :construction:
