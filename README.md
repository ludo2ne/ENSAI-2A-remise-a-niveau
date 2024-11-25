# ENSAI-2A-remise-a-niveau

Remise à niveau pour les étudiants de 2e année (21h)

## :arrow_forward: Programme

- [ ] Bases de données et SQL (3h)
- [ ] Python - initiation (6h)
- [ ] Programmation Orientée Objet (POO) (9h)
- [ ] UML (3h)
- [ ] Divers outils utiles (Markdown, VSCode...)

## :construction: TODO

- [ ] Clean repo :arrow_right: dossiers src et Outils
- [ ] Création d'arbo
- [ ] Bookmarks

### SQL

- [ ] maj SEQUENCE de la table joueurs après INSERT
- [ ] fix pour requêter hors VM

### Python

- [ ] égalité entre float (pytest approx)
- [x] join ne prend qu'un seul paramètre
- [ ] fonctions : type retour -> float, doc """, nom explicite
- [ ] Compte bancaire : clean + ajouter controles
- [ ] Protection des attributs : step 1 intro, step2 : properties pour aller plus loin

```
if type(nom) != str:
    raise TypeError(f"Attributes nom : Expected str got {type(nom)}")
```

### POO

- [ ] Slide : ajouter abstract
- [ ] TDD sur jeu de Dominos

### diapo intro

```
- Présentation
  - perso
  - scola, DSI, rôles
  - cours à l'ENSAI, matières théoriques, pratiques, étudiant diversifiés
  - ENSAI-stats sur github (tuto-R ancienne version)
  - l'info, pourquoi cette remise à niveau
  - projet info (intégration, ex : site de location de velo)
    - IHM : les menus
	- stocker vos données
	- Lien entre les 2 : services
  - contenu de la remise à niveau
  - examen date ??
- Tour de table 
  - prénom
  - où vous venez
  - que faisiez-vous l'année dernière
  - connaissances Python SQL POO
  
  
TODO :

- tester videos
- sujets en ligne
- groupes projet info
- date exam
```

## :rocket: Publier les pages

Site construit avec [Quarto](https://quarto.org/) ([Tuto](https://ludo2ne.github.io/Quarto-tuto/))

Pour générer les pages :

- en local : `quarto render` (les pages sont crées dans le dossier *_site*)
- sur [GitHub](https://ludo2ne.github.io/ENSAI-2A-remise-a-niveau/) : voir fichier `.github/workflows/publish.yml`

## Licence

Ce projet est sous licence [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/).

Vous êtes libre de partager et modifier ce travail à des fins non commerciales, à condition de me créditer et de redistribuer sous la même licence.
