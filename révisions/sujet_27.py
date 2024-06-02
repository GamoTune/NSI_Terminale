#Exercice 1

def couples_consecutifs(tab):
    lst = []
    for i in range(1, len(tab)):
        if tab[i-1] + 1 == tab[i]:
            lst.append((tab[i-1], tab[i]))
    return lst

print(couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7]))


#Exercice 2

def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return

    M[i][j] = val

    if i-1 >= 0: # propage en haut
        colore_comp1(M, i-1, j, val)
    if i+1 < len(M): # propage en bas
        colore_comp1(M, i+1, j, val) 
    if j-1 >= 0: # propage à gauche 
        colore_comp1(M, i, j-1, val) 
    if j+1 < len(M): # propage à droite 
        colore_comp1(M, i, j+1, val)


M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
colore_comp1(M, 2, 1, 3)
print(M)