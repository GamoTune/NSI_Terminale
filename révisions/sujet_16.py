#Exercice 1

def ecriture_binaire_entier_positif(n):
    if n == 0:
        return "0"
    n_bin = ""
    while n != 0:
        n_bin = str(n % 2) + n_bin
        n = n // 2
    return n_bin



print(ecriture_binaire_entier_positif(5))



#Exercice 2

def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(n):
        for j in range(n-1):
            if tab[j] > tab[j+1]:
                echange(tab, j, j+1)
    return tab


tab = [9, 3, 7, 2, 3, 1, 6]
print(tri_bulles(tab))