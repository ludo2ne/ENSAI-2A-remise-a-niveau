# R à l'ENSAI

## :arrow_forward: Introduction

**R** est un langage de programmation open-source et un environnement logiciel dédié à l'analyse statistique et graphique.  
Il offre une large gamme de fonctionnalités pour effectuer par exemple :

* des analyses de données,
* ajuster des modèles statistiques,
* créer des graphiques,
* effectuer des tests statistiques

R dispose d'une vaste [collection de packages](https://cran.r-project.org/web/packages/available_packages_by_name.html) qui étendent ses fonctionnalités. Les plus connus sont :

* **dplyr** : Ce package fournit des outils pour la manipulation et la transformation de données, notamment les opérations de filtrage, tri, regroupement, jointure...
* **ggplot2** : Ce package permet de créer des graphiques élégants et informatifs basés sur la grammaire des graphiques. Il offre une grande flexibilité pour créer des graphiques à partir de différents types de données
* **tidyr** : Ce package facilite la manipulation de la structure des données en effectuant des opérations de transformation, de regroupement et d'étalement des données

**RStudio** est un environnement de développement intégré (IDE) spécialement conçu pour travailler avec le langage R.  
Il fournit une interface conviviale et des fonctionnalités avancées pour faciliter le développement, le débogage et la visualisation des résultats en R.

---

## :arrow_forward: Config ENSAI

RStudio est disponible à différents endroits :

* installé sur les VM (Version 1.4.1717)
* cluster (Version 1.4.1717)
  * <https://clust-n1.ensai.fr/auth-sign-in>
  * <https://clust-n2.ensai.fr/auth-sign-in>
* [SSPCloud](https://datalab.sspcloud.fr/home) (2023.06.0)
  * Créer un compte avec votre mail ensai
  * Mes services > Ajouter un nouveau service > RStudio
  * :warning: Une fois votre travail terminé, sauvegardez votre code en local
    * en effet, les services sur le SSPCloud ont une durée de vie très limitée car cela coute de la ressource
    * il est d'ailleurs demandé de supprimer son service une fois le travail terminé

La puissance de calcul est beaucoup beaucoup plus grande sur les clusters et le SSPCloud.  
L'utilisation de RStudio sur la VM est déconseillée mais comme cela parait plus simple, c'est le choix de 95% des élèves...

---

## :arrow_forward: RStudio

* File > New File > RScript
  * `ech1 <- rnorm(10); ech1` par exemple pour générer 10 valeur de Loi Normale Centrée Réduite, stocker le résultat dans la variable `ech1`, puis afficher le contenu de la variable
  * CTRL + ENTREE pour éxécuter le code ci-dessus
* Les résultats s'affichent dans le terminal en bas à gauche
* En haut à gauche, sont listées les variables créées

---

## :arrow_forward: Quelques bonnes partiques

* Aérez et commentez votre code
* Utilisez des noms de variables significatifs
* Commencez tous vos scripts par `rm(list=ls())` pour nettoyer votre environnement de travail
* Pour nettoyer la console : clic dans la console puis CTRL + L
* <https://www.book.utilitr.org/02_bonnes_pratiques/01-qualite-code>

---

## :arrow_forward: Liens utiles

* <https://www.book.utilitr.org/>
* <https://teaching.slmc.fr/r/>
* <https://github.com/ludo2ne/R-tuto>

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
