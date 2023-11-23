#Exercice 1

def convertir(tab):
    x = 0
    for i in range(len(tab)):
        if tab[i] == 1:
            x += 2**(len(tab)-1-i)
    return x

print("Le nombre binaire [1, 0, 1, 0, 0, 1, 1] converti en décimal est : ", convertir([1, 0, 1, 0, 0, 1, 1]))

########################################################


## Exercice 2

liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j sert à déterminer où placer la valeur à ranger
        j = i
        # tant qu'on a pas trouvé la place de l'élément à insérer
        # on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j - 1]:
            tab[j] = tab[j-1]
            j -= 1
        tab[j] = valeur_insertion
    return tab


print("La liste [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6] trier est : ",tri_insertion(liste))