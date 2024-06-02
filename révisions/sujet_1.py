#Sujet 0

#Exercice 1

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
     'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
     'H':['','']}

def taille(arbre, lettre):
    total = 1
    if arbre[lettre][0] != '':
        total += taille(arbre, arbre[lettre][0])
    if arbre[lettre][1] != '':
        total += taille(arbre, arbre[lettre][1])
    
    return total
    

print(taille(a, 'F'))



#Exercice 2


def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.''' 
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp


def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(N):
        imin = k
        for i in range(k, N):
            if tab[i] < tab[imin]:
                imin = i
        echange(tab, imin, k)


tab = [41, 55, 21, 18, 12, 6, 25]
tri_selection(tab)
print(tab)



