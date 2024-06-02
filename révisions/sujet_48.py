#Exercice 1

adj = [[1, 2], [2], [0], [0]]

def voisins_entrants(adj, x):
    lst_adj = []
    for i in range(len(adj)):
        if x in adj[i]:
            lst_adj.append(i)
    return lst_adj

print(voisins_entrants([[1, 2], [2], [0], [0]], 1))


#Exercice 2

def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1, len(s)):
        if s[i] == chiffre:
            compte = compte + 1
        else:
            resultat += str(compte) + str(chiffre)
            chiffre = s[i]
            compte = 1
    lecture_chiffre = str(compte) + str(chiffre)
    resultat += lecture_chiffre
    return resultat

print(nombre_suivant('1211'))