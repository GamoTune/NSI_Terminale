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
    
print("La taille de l'arbre 'a' et de sommet 'F' est : ", taille(a, 'F'))

assert taille(a, 'F') == 9


print()
print("-------------------------------------")
print()


#Exercice 2


def tri_selection(tab):
    N = len(tab)
    for k in range(N):
        imin = k
        for i in range(k, N):
            if tab[i] < tab[imin]:
                imin = i
        tab[k], tab[imin] = tab[imin], tab[k]



liste = [41, 55, 21, 18, 12, 6, 25]
tri_selection(liste)
print("La liste [41, 55, 21, 18, 12, 6, 25] après tri donne : ", liste)

assert liste == [6, 12, 18, 21, 25, 41, 55]