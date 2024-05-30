#Exercice 1

def gb_vers_entier(tab):
    puissance = len(tab)
    total = 0
    for element in tab:
        puissance -= 1
        if element:
            total += 2**puissance
    return total

print(gb_vers_entier([True, False, True,
        False, False, True, True]))


#Exercice 2

def tri_insertion(tab):
    '''Trie le tableau tab par ordre croissant
    en appliquant l'algorithme de tri par insertion''' 
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j sert à déterminer
        # où placer la valeur à ranger
        j = i
        # tant qu'on n'a pas trouvé la place de l'élément à
        # insérer on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j = j - 1
        tab[j] = valeur_insertion
