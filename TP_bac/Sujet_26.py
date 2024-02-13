#Exercice 1

def multiplication(n1, n2) :
    s=0
    if n1==0 or n2==0:
        return 0
    if n1<0:
        return -multiplication(-n1,n2)
    if n2<0:
        return -multiplication(n1,-n2)
    for i in range(n2):
        s = s+n1
    return s

print("La multiplication de (3, 5) donne : ", multiplication(3, 5))
print("La multiplication de (-4, -8) donne : ", multiplication(-4, -8))
print("La multiplication de (-2, 6) donne : ", multiplication(-2, 6))
print("La multiplication de (-2, 0) donne : ", multiplication(-2, 0))

assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(-2, 0) == 0

print()
print("---------------------------------------------")
print()

#Exercice 2

def dichotomie(tab, x):
    """
    tab : tableau d'entiers trie dans l'ordre croissant
    x   : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
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
    return False

print("La dochotomie de ([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28) donne : ", dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))
print("La dochotomie de ([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27) donne : ", dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))

assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28) == True