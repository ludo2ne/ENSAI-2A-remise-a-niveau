
# Diagramme de cas d'utilisation

Un diagramme de cas d'utilisation UML (Unified Modeling Language) est un type de diagramme utilisé pour représenter les interactions entre les acteurs (utilisateurs ou systèmes externes) et le système logiciel. Il met l'accent sur les fonctionnalités fournies par le système du point de vue des utilisateurs.

Un diagramme de cas d'utilisation se compose de plusieurs éléments clés :

* **Acteur** : Un acteur représente un rôle joué par un utilisateur ou un système externe qui interagit avec le système logiciel. Il peut s'agir d'une personne, d'un autre système, d'un périphérique matériel, etc. Les acteurs sont souvent représentés par des silhouettes.
* **Cas d'utilisation** : Un cas d'utilisation représente une fonctionnalité ou une action que le système logiciel fournit à ses acteurs. Il décrit une interaction entre les acteurs et le système pour atteindre un objectif spécifique.
* **Relation d'association** : Les relations d'association connectent les acteurs aux cas d'utilisation pour montrer quel acteur utilise quel cas d'utilisation.

Les diagrammes de cas d'utilisation UML sont utilisés pour :

* capturer les exigences fonctionnelles du système
* identifier les acteurs impliqués
* décrire les interactions entre les acteurs et le système
* définir les fonctionnalités attendues du système

Ils aident à communiquer efficacement les besoins des utilisateurs et à guider le processus de développement logiciel en se concentrant sur les objectifs de l'utilisateur final.

---

## :arrow_forward: Outils

* [PlantUML](http://www.plantuml.com/)
  * [exemple](https://github.com/ludo2ne/projet-info-2A/blob/main/doc/diagrammes/diag_cas_utilisation.txt)

---

## :arrow_forward: Exemple

```mermaid
graph LR

  player[",-. \n`-' \n/|\ \n |\n/ \ \n Player"]
  organizer[",-. \n`-' \n/|\ \n |\n/ \ \n Organizer"]

  player --> modifyProfile([Modify Profile])
  player --> register([Register Tournament])
  player --> becomeArbiter([Become Arbiter])
  
  organizer --> createTournament([Create   Tournament])
  organizer --> modifyTournament([Modify Tournament])
```

<style>
    body{
        text-align: justify;
    }
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
