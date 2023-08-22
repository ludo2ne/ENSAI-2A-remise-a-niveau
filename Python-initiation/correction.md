




# Tests et boucles

## ex1

somme = 0
for i in range(1,11):
    somme += i**2
somme

## ex2

for i in range(5, -1, -1):
    print(i)
print("Boom")

## ex3

gamme = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']

i = 0
while i < len(gamme):
    print("La note numéro " + str(i) + " de la gamme de do majeur est " + gamme[i])
    i += 1
	

## ex4


liste = [34, 7, 20, 12, 50, 23, 16, 28, 6, 11, 19, 13, 26, 8, 9]
taille = len(liste)

for i in range(taille):
    for j in range(i, taille):
        if liste[i] > liste[j]:
            tmp = liste[j]
            liste[j] = liste[i]
            liste[i] = tmp
liste

## ex5

a = 0
b = 1
for i in range(10):
    print(a + b)
    b = a + b
    a = b - a

## ex6

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

def puissance(x, y):
    return x**y

print(puissance(2, 10))

## ex2

import numpy as np

def statistiques_descriptives(liste):
    return round(np.mean(liste),2), round(np.var(liste),2)

statistiques_descriptives([1,12,20,3,8,15,17])

## ex3

def est_pair(i):
    if type(i) is not int:
        print("Le paramètre " + str(i) + " n'est pas entier")
    else:
        return i%2 == 0
    
print(est_pair(12))
print(est_pair(8.5))
print(est_pair("toto"))

## ex4

def enlever_doublons(liste, trier = False):
    if trier:
        return sorted(set(liste))
    else:
        return list(set(liste))

print(enlever_doublons([1,12,1,4,4]))
print(enlever_doublons([1,12,1,4,4], True))

## ex5

def factoriel_rec(i):
    if i == 0:
        return 1
    else:
        return i * factoriel_rec(i-1)
    
factoriel_rec(5)

## ex6

def appliquer_fonction_liste(liste, fonction):
    res = [fonction(element) for element in liste]
    return res

l = ["abcd","Ensai","ReNNes"]
majuscule = lambda c:c.upper()

appliquer_fonction_liste(l, majuscule)