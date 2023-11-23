#Exercice 1

def couples_consecutifs(L):

    assert len(L) >= 2
    couples = []
    for i in range(len(L)-1):
        if L[i]+1 == L[i+1]:
            couples.append((L[i], L[i+1]))
    return couples


print("Les couples consécutife dans [1, 4, 5, 3] sont : ",couples_consecutifs([1, 4, 3, 5]))
print(couples_consecutifs([1, 4, 5, 3]))
print(couples_consecutifs([1, 1, 2, 4]))
print(couples_consecutifs([7, 1, 2, 5, 3, 4]))
print(couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7]))
assert couples_consecutifs([1, 4, 3, 5]) == []
assert couples_consecutifs([1, 4, 5, 3]) == [(4, 5)]
assert couples_consecutifs([1, 1, 2, 4]) == [(1, 2)]
assert couples_consecutifs([7, 1, 2, 5, 3, 4]) == [(1, 2), (3, 4)]
assert couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)]



#Exercice 2

def propager(M, i, j, val):
    if M[i][j] == 1:
       M[i][j] = val

    # l'element en haut fait partie de la composante
    if i-1 >= 0 and M[i-1][j] == 1:
        propager(M, i-1, j, val)

    # l'element en bas fait partie de la composante
    if i+1 < len(M) and M[i+1][j] == 1:
        propager(M, i+1, j, val)

    # l'element à gauche fait partie de la composante
    if j-1 >= 0 and M[i][j-1] == 1:
        propager(M, i, j-1,val)

    # l'element à droite fait partie de la composante
    if j+1 < len(M) and M[i][j+1]:
        propager(M, i, j+1, val)
    
    return M

M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
print(f"La propagation de 3 dans M ({M}) donne : ",propager(M, 2, 1, 3))
assert propager(M, 2, 1, 3) == [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]
