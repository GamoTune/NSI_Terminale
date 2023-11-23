#Exercise 1
def recherche_min(tab):
    min = 0 #Indice minimum
    for i in range(len(tab)): #Parcours de la table
        if tab[i] < tab[min]: #Si la valeur tester est inferieur a la valeur minimum
            min = i #Alors la valeur minimum deviens cette valeur
    return min

assert recherche_min([5]) == 0
assert recherche_min([2, 4, 1]) == 2
assert recherche_min([5, 3, 2, 2, 4]) == 2
print(f"Dans le tableau [5], l'indice de la première occurrence du minimum de ce tableau est  : {recherche_min([5])}")
print(f"Dans le tableau [2, 4, 1], l'indice de la première occurrence du minimum de ce tableau est  : {recherche_min([2, 4, 1])}")
print(f"Dans le tableau [5, 3, 2, 2, 4], l'indice de la première occurrence du minimum de ce tableau est  : {recherche_min([5, 3, 2, 2, 4])}")


#EXERCIE 2
def separe(tab):

    gauche = 0
    droite = len(tab)-1
    while gauche < droite :
        if tab[gauche] == 0 :
            gauche += 1
        else :
            tab[gauche], tab[droite] = tab[droite], tab[gauche]
            droite -= 1
    return tab

assert separe([1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]
assert separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

print(f"Le tableau trier de [1, 0, 1, 0, 1, 0, 1, 0] est : {separe([1, 0, 1, 0, 1, 0, 1, 0])}")
print(f"Le tableau trier de [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0] est : {separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0])}")

