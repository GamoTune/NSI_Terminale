#Exercice 1
def recherche(elt, tab):
    if elt in tab:
        for i in range(len(tab)):
            if tab[i] == elt: return i
    else: return -1


print(recherche(1, [2, 3, 4]))
print(recherche(1, [10, 12, 1, 56]))
print(recherche(50, [1, 50, 1]))
print(recherche(15, [8, 9, 10, 15]))
print(recherche(50, []))
print(recherche(4, [2, 4, 4, 3, 4]))


print("")





#Exercice 2
def insere(a, tab):
    """ Insère l'élément a (int) dans le tableau tab (list)
        trié par ordre croissant à sa place et renvoie le
        nouveau tableau."""
    l = list(tab) #l contient les memes elements que tab
    l.append(a)
    i = len(l) - 2
    while a < l[i] and i >= 0:
        l[i+1] = l[i]
        l[i] = a
        i -= 1
    return l


print(insere(3, [1, 2, 4, 5]))