# R à l'ENSAI

### Introduction

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

### Liens utiles

* <https://www.book.utilitr.org/>
* <https://github.com/ludo2ne/R-tuto>

---

# Config ENSAI

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

### RStudio sur la VM

Le principal inconvénient est lié à l'utilisation de packages.
Pour réaliser vos travaux, vous allez avoir besoin d'une multitude de packages, et donc de les télécharger.
Et si l'on ne fait pas attention, ces packages s'installent automatiquement sur votre disque personnel `P:/` qui n'a que peu d'espace libre.

La solution est d'installer ces packages dans le `C:/`. Ce disque qui n'est pas sauvegardé mais peu importe, si par grande malchance vous perdez vos packages, il suffira de les réinstaller.

##### Définir l'endroit où stocker les packages R

* Créer un dossier `C:/users/idXXXX/R`
* Aller dans `P:/`
  * afficher les fichiers cachés
  * Créer ou modifier le fichier `.Rprofile` en ajoutant le code ci-dessous

```r
# Get the default library path
default_lib_path <- paste0("C:",Sys.getenv("HOMEPATH"), "\\R")     # correspond à C:/users/idXXXX/R

# Add the default library path to .libPaths()
if (default_lib_path != "") {
  .libPaths(c(default_lib_path, .libPaths()))
}
```

* Ouvrez RStudio
  * vérifiez que le dossier créé ci-dessus est bien dans le libpath avec la commande `.libPaths()`
  * testez l'installation d'un package `install.packages("dplyr")`
  * vérifiez dans la console que le package s'installe dans le dossier créé ci-dessus
  * listez les packages disponibles `library()`
* Chargez le package
  * Pour utiliser un package, il ne suffit pas de l'installer (l'installation c'est une seule fois)
  * par contre il faut le charger à chaque session `library(dplyr)`

---

# Quelques bonnes partiques

* Aérez et commentez votre code
* Utilisez des noms de variables significatifs
* Commencez tous vos scripts par `rm(list=ls())` pour nettoyer votre environnement de travail
* Pour nettoyer la console : clic dans la console puis CTRL + L
* <https://www.book.utilitr.org/02_bonnes_pratiques/01-qualite-code>
