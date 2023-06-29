# Initiation aux commandes Bash

Il y a peu, dans un monde proche, très proche la ligne de commande était le seul moyen de transmettre ses instructions à un ordinateur. Pas de souris, pas de bureau avec des icones, simplement un clavier et un terminal.

Dans de nombreux domaines de l'informatique, les instructions se donnent toujours en lignes de commande. En effet, créer des interfaces graphiques est couteux et plus difficile à maintenir.

Nous allons ici présenter quelques commandes simples, connues et utilisées par tout informaticien. Chez windows il y a 2 terminaux disponibles :

* [cmd](https://fr.wikipedia.org/wiki/Cmd), l'invite de commande "historique"
* [powershell](https://fr.wikipedia.org/wiki/Windows_PowerShell), plus récent

Cependant, nous nous interesserons ici à la sphère Unix beaucoup plus populaire. Il y a également différents interpréteurs, le plus utilisé étant [Bash](https://fr.wikipedia.org/wiki/Bourne-Again_shell). Les commandes présentées ici sont standardisées et compréhensibles par n'importe quel interpréteur Unix (et sont même parfois identiques chez Windows)

En tant que Data Scientist on ne vous demandera pas de savoir pirater la CIA avec une Casio Collège. Cependant, connaitre ces commandes est un **must-have** qui vous servira à coup sûr.

---

## :arrow_forward: Apprendre à naviguer

Il ne s'agit pas d'apprendre à faire un noeud de chaise, mais de savoir parcourir les dossiers et les fichiers de votre machine.

* Ouvrir un terminal Bash
  * Par exemple Git Bash
* Ecire la commande **`pwd`** puis ENTREE
  * un faux ami : cela ne signifie pas password mais **print working directory**
  * normalement le résultat de cette commande est `/p/`
  * vous êtes donc à la racine du lecteur `/p`, votre espace personnel
* **`ls`** pour **lister**
  * affiche les dossiers et fichiers de l'endroit où vous êtes (en l'occurence `/p`)
  * **`ls -l`** pour afficher en colonne (plus joli), et affiche d'autres informations telles le nom du propriétaire du fichier, la date de modification, les droits en lecture, écriture...
    * **`ll`** : souvent cet alias à `ls -l` existe
    * cela signifie que pour l'interpréteur `ll` ou `ls -l`, c'est pareil
    * mais `ll` c'est plus rapide à taper
    * `alias` : affiche la liste des alias
  * Le `-l` est donc une option de la commande `ls`
  * Chaque commande a de nombreuses options, internet est votre ami si besoin
* **`cd 'Ma musique'`**
  * cd = change directory
  * le terminal affiche votre nouvel emplacement : `/p/Ma musique`
  * lorsqu'il y a des espaces dans un nom de dossier, il faut ajouter des  guillemets simples ' ou doubles " autour du nom du dossier
* `pwd`
* `ls`
* **`cd ..`**
  * pour revenir au dossier parent
* `cd /c`
  * pour changer de lecteur et aller sur le disque C:/
* `ls`
* `cd /p`
  * revenir au lecteur P pour la suite

Avec les 3 commandes décrites ci-dessus (pwd, ls et cd) vous pouvez naviguer sereinement dans les dossiers.

---

## :arrow_forward: Quelques trucs et astuces

Voici des raccourcis clavier bien utiles :

* **FLECHE HAUT** : historique des commandes lancées
  * utile pour éviter de réécrire en entier une commande que l'on a lancée 2 min avant
  * FLECHE BAS : également pour parcourir l'historique mais dans le sens inverse
* `history` : historique des commandes exécutées
* **TAB** : autocompletion
  * `cd Ma` puis TAB
  * le terminal va tenter de "compléter" la commande que vous êtes en train d'écrire
  * Comme il n'y a qu'un seul dossier commençant par "Ma", en faisant TAB, le terminal va ajouter pour obtenir `cd Ma\ musique` (= `cd "Ma musique"`)
* **CTRL + C** : pour stopper la commande en cours si elle est trop longue
* **CLIC Molette** (ou parfois CLIC droit, ou encore SHIFT + INSER) : Coller

---

## :arrow_forward: Manipuler fichiers et dossiers

* `cd /p`
* **`mkdir -p Cours/Informatique/bash-tp`**
  * mkdir = make directory
  * Cette commande crée le dossier `bash-tp`
  * `-p` permet de créer les dossiers parents (Cours et Informatique) s'ils n'existent pas
* `cd Cours/Informatique/bash-tp`
  * Pour aller dans le dossier que l'on vient de créer
* **`touch a.txt`**
  * créer un fichier vide nommé `a.txt`
* Pour écrire dans un fichier il y a de nombreuses possibilités, par exemple avec l'[éditeur vi](https://fr.wikipedia.org/wiki/Vi)
  * Cependant l'utilisation de `vi` est loin d'être triviale
  * Si vous trouvez que ce TP est déjà assez compliqué comme ça, ne touchez pas à `vi`
  * Si vous êtes trop curieux, que vous avez ouvert le fichier a.txt avec `vi` et que maintenant vous êtes bloqué, tapez `:q!` pour sortir
* Pour info d'autres éditeurs :
  * Nano moins connu mais qui a l'air plus intuitif : `nano a.txt` (CTRL + X pour quitter)
  * Si vous avez lancé votre terminal sous Windows : `notepad a.txt`
* **`rm a.txt`**
  * rm = remove pour supprimer le fichier
  * :warning: attention à bien utiliser cette commande, risque de perte de données
* **`ls -l /c > b.txt`**
  * Exécute la commande `ls -l /c` qui liste tous les fichiers et dossiers du lecteur /c
  * Puis le > indique que l'on sauvegarde le résultat dans le fichier b.txt créé s'il n'existe pas
* **`cat b.txt`**
  * affiche le fichier
  * `head b.txt` : affiche uniquement les 10 premières lignes
  * `tail b.txt` : affiche uniquement les 10 dernières lignes
* `pwd >> b.txt`
  * S'il y avait un seul `>` : le contenu du fichier b.txt serait écrasé
  * avec 2 `>>` : le résultat de la commande pwd est ajouté à la fin du fichier sans écraser ce qu'il y avait avant
  * `cat b.txt`
    * on voit que le fichier b.txt contient :
      * d'abord le résultat de la commande `ls -l /c`
      * puis celui de la commande `pwd`
* **`cp b.txt b1.txt`**
  * Crée une copie du fichier b.txt dans le fichier b1.txt
* **`mv b1.txt b2.txt`**
  * mv = move pour renommer le fichier b1.txt en b2.txt
* **`grep Program b.txt`**
  * grep = Global Regular Expression Print
  * L'exemple ci-dessus recherche dans le fichier b.txt toutes les lignes contenant le mot `Program` et les affiche
  * Ou sinon comme le nom de la commande l'indique vous pouvez utiliser des expressions régulières si vous aimez ça
* **`ls -l /c | grep Program`**
  * le résultat est le même que la dernière commande
  * le terminal exécute la première commande `ls -l /c` et stocke le résultat
  * le pipe | signifie que ce résultat est transféré à la commande suivante pour application (il est possible d'en enchainer plusieurs)
  * Ainsi dans un second temps, le terminal exécute :
    * `grep Program "résultat première commande"`
  * `f(x) | g` :arrow_right: traduit en langage matheux donne : g(f(x))

---

## :arrow_forward: Résumé

les commandes qu'il faut retenir et savoir utiliser

| | |
| ------------- | ------------------------------------- |
| pwd           | Pour savoir où on est                 |
| ls            | Pour lister ce qu'il y a              |
| cd "dossier"  | Pour se déplacer vers un sous-dossier |
| cd ..         | Pour aller dans le dossier parent     |
| cat "fichier" | Pour voir le contenu d'un fichier     |

---

## :arrow_forward: Un petit exercice d'application

1. Aller dans le dossier `/p/Cours/Informatique/bash-tp`
2. Créer un dossier `exo1` et aller dans ce dossier (commandes : `mkdir, cd`)
3. Lister en lignes tous les fichiers et dossiers de `/C/Program Files` (`ls -l`)
4. Stocker le résultat de la commande précédente dans le dossier exo1, fichier `liste_programmes.txt` (utiliser `>`)
5. Renommer ce fichier en `prog.txt` (`mv`)
6. Afficher le contenu de ce fichier (`cat`)
7. Compléter la commande précédente pour avoir uniquement les lignes contenant la lettre `m` (`|` et `grep`)
8. Compléter la commande précédente pour trier (commande `sort`)
9. Compléter la commande précédente pour ne garder que les 3 premières lignes (`head -3`)
10. Copier le fichier `prog.txt` dans `/p/Cours/Informatique/bash-tp` (commande `cp` et utiliser `..` pour accéder au dossier parent)

...  
...  
...  
...  
...  
...  
...  
...  
...  
...  
...  
...  
...  
...  
...  
...  
...  
...  
...  
...
  
Solution

```bash=
cd Cours/Informatique/bash-tp
mkdir exo1
ls -l "/C/Program Files"
ls -l "/C/Program Files" > liste_programmes.txt
mv liste_programmes.txt prog.txt
cat prog.txt
cat prog.txt | grep m
cat prog.txt | grep m | sort
cat prog.txt | grep m | sort | head -3
cp prog.txt ..
```
