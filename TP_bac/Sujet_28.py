#Exercice 1

def moyenne (tab) -> float:

    n_value = len(tab)
    somme = 0
    for i in range(n_value):
        somme += tab[i]
    
    
    return somme / n_value

print("La moyenne de [1] donne : ", moyenne([1]))
print("La moyenne de [1, 2, 3, 4, 5, 6, 7] donne : ", moyenne([1, 2, 3, 4, 5, 6, 7]))
print("La moyenne de [1, 2] donne : ", moyenne([1, 2]))

assert moyenne([1]) == 1
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4
assert moyenne([1, 2]) == 1.5



print()
print("-------------------------------------------------------")
print()


#Exercice 2
def dichotomie(tab, x):
    """
        tab : tableau trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if len(tab) == 0:
        return False, 1

    # cas où x n'est pas compris entre les valeurs extrêmes
    if (x < tab[0]) or (x > tab[-1]):
        return False, 2
    
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False, 3


print("Y a t'il la valeur 28 dans [15, 16, 18, 19, 23, 24, 28, 29, 31, 33] ? : ", dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))
print("Y a t'il la valeur 27 dans [15, 16, 18, 19, 23, 24, 28, 29, 31, 33] ? : ", dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))
print("Y a t'il la valeur 1 dans [15, 16, 18, 19, 23, 24, 28, 29, 31, 33] ? : ", dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1))
print("Y a t'il la valeur 28 dans [] ? : ", dichotomie([], 28))


assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27) == (False, 3)
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1) == (False, 2)
assert dichotomie([], 28) == (False, 1)