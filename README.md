# ENSAI-2A-remise-a-niveau

Remise à niveau pour les étudiants de 2e année (21h)

## :arrow_forward: Programme

Ce répo contient des ressources pour introduire les items suivants :

- [ ] Bases de données et SQL (3h)
- [ ] Python - initiation (6h)
- [ ] Programmation Orientée Objet (POO) (9h)
- [ ] UML (3h)
- [ ] Divers outils utiles (git, markdown, R...)

## :arrow_forward: Comment utiliser les ressources de ce dépôt ?

### :small_orange_diamond: 1. Inititation à SQL

Dans le dossier `SQL`

- [ ] lire le fichier `SQL.md`
- [ ] faire l'exercice
- la correction est disponible dans le dossier `SQL/exo`

### :small_orange_diamond: 2. Initiation à Python

Vous pouvez commencer par créer un clone de ce dépôt sur votre machine :

- Ouvrez **Git Bash**, puis coller les commandes suivantes
- `mkdir -p /p/Cours2A/UE3_Remise_a_niveau && cd $_`
- `git clone https://github.com/ludo2ne/ENSAI-2A-remise-a-niveau.git`
- cela crée une copie du dépôt dans P:/Cours2A/UE3_Remise_a_niveau/ENSAI-2A-remise-a-niveau

---

- [ ] Lire et suivre les consignes données dans le fichier `Python-initiation/Python.md`
  - [ ] Importer dans Jupyter les 5 notebooks, lire, puis faire les exercices

### :small_orange_diamond: 3. Programmation Orientée Objet

- [ ] Lire et suivre les consignes données dans le fichier `Python-POO/La POO.md`
- [ ] Faire les exercices

### :small_orange_diamond: 4. UML

Lire dans cet ordre les fichiers du dossier `UML` :

- [ ] `UML.md`
- [ ] `Diag cas utilisation.md`
- [ ] `Diag classe.md`
  - [ ] faire l'exercice

---

## :arrow_forward: Alternatives

Voici d'autres possibilités pour se mettre à niveau en Python, POO et SQL

### 1. Vidéos de la session 2022-2023

si vous avez vos accès à l'ENT ENSAI, les vidéos de la session de l'année dernière sont disponibles ici :

- https://foad-moodle.ensai.fr/mod/url/view.php?id=11354

### 2. Cours en ligne pour apprendre Python et SQL

- SQL
  - https://openclassrooms.com/fr/courses/7818671-requetez-une-base-de-donnees-avec-sql
- Python
  - https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python#table-of-content
    - parties 1 et 2
  - https://openclassrooms.com/fr/courses/7150616-apprenez-la-programmation-orientee-objet-avec-python
    - parties 1 et 2


## Publier les pages

Site construit avec [Quarto](https://quarto.org/) ([Tuto](https://ludo2ne.github.io/Quarto-tuto/))

Pour générer les pages :

- en local : `quarto render` (les pages sont crées dans le dossier *_site*)
- sur [GitHub](https://ludo2ne.github.io/ENSAI-2A-remise-a-niveau/) : voir fichier `.github/workflows/publish.yml`
