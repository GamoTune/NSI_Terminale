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
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]

        j = i

        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j = j - 1
        tab[j] = valeur_insertion
    return tab


tab = [98, 12, 104, 23, 131, 9]
print(tri_insertion(tab))