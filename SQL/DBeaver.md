# Outils de gestion des SGBD

## :arrow_forward: DBeaver

> DBeaver est un outil de gestion de base de données multiplateforme et open source. Il offre une interface graphique conviviale pour se connecter, gérer et requêter différentes bases de données, notamment MySQL, PostgreSQL, Oracle, SQL Server, SQLite, et bien d'autres encore.

Ouvrez le logiciel DBeaver installé sur votre VM, puis suivez les indications ci-dessous.

### :small_orange_diamond: Configuration

* Menu Fenêtre > Preference
  * Formatage SQL
    * Casse des mots clefs : `UPPER`
    * [x] Insert spaces for tabs
    * Appliquer
  * Metadonnées
    * Décocher "Ouvrir une connexion séparée pour la lecture des étadonnées"
  * Editeur SQL
    * Décocher "Ouvrir une connexion séparée pour chaque éditeur"
  * Templates (OPTIONNEL)
    * Enlever les modèles existants
    * Importer le fichier `templates_dbeaver.xml`
    * Les templates permettent d'écrire plus rapidement des requêtes

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

Une autre solution pour éxécuter des requêtes SQL est de passer par l'interface [pgAdmin](http://sgbd-eleves.domensai.ecole/phppgadmin/)

* Utilisateur : idxxxx
* Mot de passe : idxxxx
* Une fois connecté, cliquez sur `idxxxx` dans le menu de gauche
* cliquez sur `SQL` pour exécuter des requêtes

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
