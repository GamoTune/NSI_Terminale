#Exercice 1

def moyenne(tab):
    nombre = len(tab)
    resultat = 0
    for i in tab:
        resultat += i
    return resultat/nombre

print(moyenne([1,2]))


#Exercice 2

def dichotomie(tab, x):
    """applique une recherche dichotomique pour déterminer
    si x est dans le tableau trié tab.
    La fonction renvoie True si tab contient x et False sinon"""

    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m+1
        else:
            fin = m-1
    return False

print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))