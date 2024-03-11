#Exercice 1

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
 'H':['','']}


def taille(arbre, lettre):
    noeud = arbre[lettre]
    if noeud[0] != '' and noeud[1] != '':
        return 1 + taille(arbre, noeud[0]) + taille(arbre, noeud[1])
    elif noeud[0] != '':
        return 1 + taille(arbre, noeud[0])
    elif noeud[1] != '':
        return 1 + taille(arbre, noeud[1])
    else:
        return 1
    
print(taille(a, 'F'))





print()


#Exercice 2






"""

def tri_selection(tab):
    N = len(tab)
    for k in range(...):
        imin = ...
        for i in range(... , N):
            if tab[i] < ... :
                imin = i
        ... , tab[imin] = tab[imin] , ...

"""