#Exercice 1

def recherche(elt, tab):
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    return None

#Exercice 2

def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a
                        # suivi des éléments de tab
    i = 0
    while i < len(tab_a) and a > tab[i]:
        tab_a[i] = tab_a[i+1]
        tab_a[i+1] = a
        i = i + 1
    return tab_a

print(insere([1, 2, 4, 5], 3))