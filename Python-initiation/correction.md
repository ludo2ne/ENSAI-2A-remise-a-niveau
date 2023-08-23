




# Tests et boucles

## ex1

```python
somme = 0
for i in range(1,11):
    somme += i**2
somme
```

## ex2

```python
for i in range(5, -1, -1):
    print(i)
print("Boom")
```

## ex3

```python
gamme = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']

i = 0
while i < len(gamme):
    print("La note numéro " + str(i) + " de la gamme de do majeur est " + gamme[i])
    i += 1
```
	

## ex4


```python
liste = [34, 7, 20, 12, 50, 23, 16, 28, 6, 11, 19, 13, 26, 8, 9]
taille = len(liste)

for i in range(taille):
    for j in range(i, taille):
        if liste[i] > liste[j]:
            tmp = liste[j]
            liste[j] = liste[i]
            liste[i] = tmp
liste
```

## ex5

```python
a = 0
b = 1
for i in range(10):
    print(a + b)
    b = a + b
    a = b - a
```

## ex6

```python
x = [8, 18, 6, 0, 15, 17.5, 9, 1]
minimum = float('inf')
maximum = -float('inf')

for i in x:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
        
print("max : " + str(maximum))
print("min : " + str(minimum))
```

## ex7

```python
# Testez votre réponse dans cette cellule
for eleve in notes:
    print(eleve, end = ' : ')
    nb_notes = 0
    somme = 0
    for note in notes[eleve]:
        nb_notes += 1
        somme += note
    print(somme/nb_notes)
```




# Fonctions

## ex1

```python
def puissance(x, y):
    return x**y

print(puissance(2, 10))
```

## ex2

```python
import numpy as np

def statistiques_descriptives(liste):
    return round(np.mean(liste),2), round(np.var(liste),2)

statistiques_descriptives([1,12,20,3,8,15,17])
```

## ex3

```python
def est_pair(i):
    if type(i) is not int:
        print("Le paramètre " + str(i) + " n'est pas entier")
    else:
        return i%2 == 0
    
print(est_pair(12))
print(est_pair(8.5))
print(est_pair("toto"))
```

## ex4

```python
def enlever_doublons(liste, trier = False):
    if trier:
        return sorted(set(liste))
    else:
        return list(set(liste))

print(enlever_doublons([1,12,1,4,4]))
print(enlever_doublons([1,12,1,4,4], True))
```

## ex5

```python
def factoriel_rec(i):
    if i == 0:
        return 1
    else:
        return i * factoriel_rec(i-1)
    
factoriel_rec(5)
```

## ex6

```python
def appliquer_fonction_liste(liste, fonction):
    res = [fonction(element) for element in liste]
    return res

l = ["abcd","Ensai","ReNNes"]
majuscule = lambda c:c.upper()

appliquer_fonction_liste(l, majuscule)
```


# POO

## ex1

```python
# by ChatGPT

class Etudiant:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.liste_notes = []

    def ajouter_note(self, note):
        self.liste_notes.append(note)

    def calculer_moyenne(self):
        if len(self.liste_notes) == 0:
            return 0
        total = sum(self.liste_notes)
        moyenne = total / len(self.liste_notes)
        return moyenne

# Exemple d'utilisation
etudiant1 = Etudiant("Alice", 20)
etudiant1.ajouter_note(15)
etudiant1.ajouter_note(18)
etudiant1.ajouter_note(12)
moyenne_etudiant1 = etudiant1.calculer_moyenne()
print(f"Moyenne de {etudiant1.nom}: {moyenne_etudiant1}")
```



## ex2

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, autrePoint):
        return math.sqrt((self.x - autrePoint.x)**2 + (self.y - autrePoint.y)**2)
    
p1 = Point(0,0)
p2 = Point(1,1)
print(p1.distance(p2))

class Cercle:
    def __init__(self, p_centre, p_rayon):
        self.centre = p_centre
        self.rayon = p_rayon
        
    def calculer_surface(self):
        return math.pi * self.rayon**2
    
c1 = Cercle(p1, 2)
print(c1.calculer_surface())
```


## ex3

# Testez votre réponse dans cette cellule
class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
        
    def afficher_solde(self):
        print("Le solde du compte de " + self.titulaire + " est " + str(self.solde) + " euros.")
        
    def deposer(self, montant):
        self.solde += montant
    
    def retirer(self, montant):
        if self.solde >= montant:
            self.solde -= montant
            print("Retrait accepté.")
        else:
            print("Retrait refusé : fonds insuffisants.")
            
    def transferer(self, autreCompte, montant):
        if self.solde >= montant:
            autreCompte.solde += montant
            self.solde -= montant
        else:
            print("Transfert refusé : fonds insuffisants.")
            
client1 = CompteBancaire("Bernard", 2000)
client2 = CompteBancaire("Bianca", 5000)

client1.afficher_solde()
client2.afficher_solde()

print()  # saut de ligne

client1.deposer(1000)
client1.afficher_solde() # +1000

print()

client2.retirer(6000)
client2.afficher_solde() # aucun changement

print()

client2.retirer(1000)
client2.afficher_solde() # -1000

print()

client2.transferer(client1, 5000)
client2.afficher_solde() # aucun changement

print()

client2.transferer(client1, 2000)
client2.afficher_solde() # - 2000
client1.afficher_solde() # + 2000