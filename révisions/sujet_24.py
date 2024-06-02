#Exercice 1

def parcours_largeur(arb):
    parcours = []
    file = [arb]
    while file:
        a = file.pop(0)
        parcours.append(a[1])
        if a[0] != None:
            file.append(a[0])
        if a[2] != None:
            file.append(a[2])
    return parcours



arbre = ( ( (None, 1, None), 2, (None, 3, None) ), 4, ( (None, 5, None), 6, (None, 7, None) ) )
print(parcours_largeur(arbre))
print()

#Exercice 2

def somme_max(tab):
    n = len(tab)
    sommes_max = [0]*n
    sommes_max[0] = tab[0]
    # on calcule la plus grande somme se terminant en i
    for i in range(1,n):
        if sommes_max[i-1] + tab[i] > tab[i]:
            sommes_max[i] = sommes_max[i-1] + tab[i]
        else:
            sommes_max[i] = tab[i]
    # on en déduit la plus grande somme de celles-ci
    maximum = 0
    for i in range(1, n):
        if sommes_max[i] > sommes_max[maximum]:
            maximum = i



    return sommes_max[maximum]
print()

print(somme_max([1, -2, 3, 10, -4, 7, 2, -5]))