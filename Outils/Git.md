# Introduction à Git

## :arrow_forward: Objectifs

* [ ] Comprendre le principe et l'utilité de Git
* [ ] Configurer Git
* [ ] Créer un compte GitLab
* [ ] Manipuler avec les commandes de base (clone, status, add, commit, pull, push)
* [ ] Gérer un conflit

---

### :small_orange_diamond: Ressources

* [Git TP](https://hackmd.io/BdGZF6qOTk2qvzAlvrz_WA)
* <https://github.com/InseeFrLab/formation-git>
* <https://github.com/InseeFrLab/formation-bonnes-pratiques-git-R>

---

## :arrow_forward: Git présentation

### :small_orange_diamond: Git, ça sert à quoi ?

* Git
  * Logiciel de gestion de versions
  * Logiciel libre
  * créé par Linus Torvalds, qui n'est pas n'importe qui : également créateur du noyau Linux
* Git Bash
  * Terminal pour écrire des commandes **git**
* GitLab
  * Logiciel permettant de gérer des fichiers (dépôt)
  * Partagé par plusieurs personnes
  * S'utilise avec Git
  * Propose d'autres fonctionnalités (wiki, gestion des incidents...)

### :small_orange_diamond: Pourquoi utiliser un outil de gestion de version ?

Est-ce que vous préférez avoir ceci ?

```
├───Projet info
│   ├───Livrables
│   │   ├───Rapport.tex
│   │   ├───Rapport_Ludo.tex
│   │   ├───Rapport_v1.0.tex
│   │   └───Rapport_v1.2.tex
│   ├───Rapport_old.tex
│   ├───Rapport_2022.05.15.tex
│   └───Rapport_2022.05.15_new.tex
```

Ou un seul fichier avec accès à l'historique des modifications ?

```
├───Projet info
│   └───Livrables
│     └───Rapport.tex

Historique des modifications de Rapport.tex
Date         Heure   Auteur      Message commit
----         -----   ------      --------------
2022.05.29   23h58   bianca      "Version finale"
2022.05.29   23h40   archibald   "j'avais oublié l'intro"
2022.05.29   21h32   tryphon     "ajout partie 2"
2022.05.29   20h25   bianca      "v1.1"
2022.05.29   20h12   tryphon     "Création du rapport"
```

Git permet de créer des points de sauvegardes (**commit**). Ainsi pour chaque fichier il est possible de consulter une version précédente et éventuellement de revenir en arrière en cas d'erreur.

### :small_orange_diamond: Principe général de Git

* Avec Git, vous allez avoir plusieurs dépôts de fichiers
  * un dépôt commun (dépôt distant)
  * un dépôt par contributeur (dépôts locaux)
* Git va aider synchroniser ces dépôts
  * la synchronisation n'est pas automatique
  * c'est à vous de dire quand vous voulez le faire avec des commandes git

### :small_orange_diamond: Exemples

#### Exemple 1

* Si sur le dépôt distant, le fichier `soleil.txt` a été créé par une autre personne
* La commande `git pull` permet de mettre à jour son dépôt local
* Le fichier `soleil.txt` apparait sur votre dépôt local

#### Exemple 2

* En local, vous avez créé le fichier `temple.py` et modifié le fichier `soleil.txt`
* Faites `git add .` pour les faire reconnaitre par Git
* Créez un point de sauvegarde avec la commande `git commit`
* Puis, la commande `git push` permet de partager cette nouvelle version sur le dépôt distant
* Sur le dépôt distant, les 2 fichiers seront créés ou mis à jour

Pour gérer les versions, Git utilise des points de sauvegarde appelés **commits**. Grace à cela, il est possible de consulter les versions antérieures des fichiers.

### :small_orange_diamond: Les 5 commandes qu'il faudra retenir

* **git status** : voir où l'on en est
* **git add** : ajouter de nouveaux fichiers dans le dépôt
* **git commit** : créer un point de sauvegarde
* **git pull** : mettre à jour son dépôt local en synchronisant avec le dépôt distant
* **git push** : mettre à jour le dépôt distant avec les modifications faites en local

### :small_orange_diamond: Schéma simplifié des liens entre dépôt local et dépôt distant

![](https://i.imgur.com/QsermR0.png)

* Git distingue plusieurs états de votre dépôt local mais vous pouvez considérer que les 3 dépôts de gauche forment votre dépôt local
* Comme visible sur le schéma la commande `git commit -a` permet de combiner les 2 commandes `add` et `commit` en une seule

---

## :arrow_forward: Paramètrer Git

:information_source: Le paramètrage de Git n'est pas très drôle et peut faire un peu peur. Mais pas de panique, c'est à faire une et une seule fois sur votre machine !

### :small_orange_diamond: 1. Configuration Git Bash

Git Bash est un Terminal où l'on peut écrire des commandes git.

Ouvrir **Git Bash** et entrer une à une les commandes suivantes

```bash
git config --global user.name "Prenom Nom"
git config --global user.email prenom.nom@eleve.ensai.fr
git config -l
```

La dernière commande permet de vérifier que les 2 attributs `user.name` et `user.email` sont bien renseignés

### :small_orange_diamond: 2. Clé SSH

Afin de pouvoir faire des mises à jour sur le dépôt distant, il faut que votre machine (locale) soit reconnue. Vous devez donc fournir une clé d'authentification à GitLab.

Toujours dans Git Bash, lancer une à une ces 2 commandes. La première commande permet de générer une clé publique SSH. La seconde permet de récupérer la valeur de cette clé.

```bash
ssh-keygen -t rsa -b 4096 -C "prenom.nom@eleve.ensai.fr"

## tapez ENTREE à chaque question

## Récupérez le contenu de la clé avec la commande cat
cat $HOME/.ssh/id_rsa.pub ## ou cat /c/Users/idxxxx/.ssh/id_rsa.pub
```

* La commande cat renvoie tout le contenu de ce fichier
  * En cas d'échec, vous pouvez aller dans le dossier caché `C:/Users/idxxxx/.ssh/` et ouvrir avec Notepad le fichier `id_rsa.pub`
  * si vous ne trouvez toujours pas le fichier `id_rsa.pub`, retournez voir le résultat de la commande `ssh-keygen`, il est écrit dans quel dossier la clé a été générée
* Sélectionner ce contenu et le copier dans notepad pour la prochaine étape

#### Créez une copie de votre clé

Il arrive que le dossier `C:/Users/idxxxx/.ssh` soit supprimé.  
Il est interessant d'avoir une copie de cette clé pour la restaurer si besoin.

* `cp -r $HOME/.ssh /p` pour copier le dossier dans le disque P:

> * [ ] TODO  
>
> :warning: il peut y avoir des soucis de clés ssh
>
> * la commande `ssh-keygen` crée par défaut la clé dans `/c/Users/id1965/.> ssh/id_rsa`
> * or cette clé est supprimée à chaque nouvelle ouverture de session
>   * [ ] Voir avec la DSI si possible de corriger
>
> une autre solution perenne serait de générer la clé dans /p/.ssh
> puis de définir ce path comme un endroit ou chercher un clé ssh en cas > de besoin
>
> ```bash
> eval `ssh-agent -s`    # Pour demarrer l agent ssh
> ssh-add /p/.ssh/id_rsa   # pour ajouter ce path lors de la recherche de > cle ssh
> 
> ## pb : le ssh-add est lié à la session, et devrait être refait à chaque > nouvelle session
> ssh-add -K /p/.ssh/id_rsa   # -K pour keep et éviter de refaire à chaque > session
> ## Souci car ça demande : Enter PIN for authenticator... ?!
> ```

---

### :small_orange_diamond: 3. Créer un compte sur GitLab

[GitLab](https://gitlab.com/gitlab-org/gitlab) est le site qui permet d'héberger le dépôt distant du code ([Créer un compte](https://gitlab.com/users/sign_up))

### :small_orange_diamond: 4. Déclarer votre clé publique SSH à GitLab

* Dans GitLab, aller dans **Preferences** (en haut à droite) puis dans **SSH Keys**
  * ou directement [ici](https://gitlab.com/-/profile/keys)
  * Key : coller le résultat de l'étape 2
  * Add SSH Key

:rainbow:  Bravo le paramètrage est terminé :confetti_ball:

### :small_orange_diamond: 5. En cas d'erreurs

#### The authenticity of host xxx can't be established

```
The authenticity of host 'github.com (140.82.121.4)' can't be established.  
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.    

Please make sure you have the correct access rights
and the repository exists.
```

1. Vérifiez que le dossier `C:/users/idxxxx/.ssh` existe et contient les fichiers `id_rsa` et `id_rsa.pub`. Si oui passer à l'étape 2.

Si non, recopiez votre clé dans `C:/users/idxxxx/.ssh` à partir de la sauvegarde que vous avez faite dans `P:/.ssh` lors de la création de la clé. Pour automatiser ceci, vous pouvez créer un script `restore_ssh.bat` sur le bureau contenant le code ci-dessous :

```bash
set "source=P:\.ssh"
set "destination=%HOME%\.ssh"
xcopy /E /H /I /Y "%source%" "%destination%"
pause
```

2. Vérifiez que la clé `id_rsa.pub` est bien déclarée dans GitLab ou GitHub.
Si le problème persiste, regénérez une nouvelle clé ssh et déclarez là dans GitHub ou GitLab.

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
