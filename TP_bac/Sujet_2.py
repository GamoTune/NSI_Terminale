#Exercice 1

def indices_maxi(tab):
    max = tab[0]
    indices = [0]
    for index in range(1, len(tab)):
        if max < tab[index]:
            max = tab[index]
            indices = [index]
        elif max == tab[index]:
            indices.append(index)
    return max, indices

print("L'indice maxi dans [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] est : ", indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])[0], " et ces indices sont : ", indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])[1])
print("L'indice maxi dans [1, 5, 6, 9, 1, 2, 3, 7, 9, 8] est : ", indices_maxi([7])[0], " et ces indices sont : ", indices_maxi([7])[1])

assert indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, [3,8])
assert indices_maxi([7]) == (7, [0])

print()
#Exercice 2

def positif(pile):
    pile_1 = list(pile)
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1


print("Les nombres positifs dans la liste [-1, 0, 5, -3, 4, -6, 10, 9, -8] sont : ",positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]))
print("Les nombres positifs dans la liste [-2] sont : ",positif([-2]))

assert positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]) == [0, 5, 4, 10, 9]
assert positif([-2]) == []