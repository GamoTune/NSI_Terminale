#Exercise 1
#Trie par selection

def tri_selection(tab):
    '''
    Trie tab par ordre croissant
    '''
    n=len(tab)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if tab[j]<tab[min]:
                min=j
        tab[i],tab[min]=tab[min],tab[i]
    return tab

assert tri_selection([1,52,6,-9,12]) == [-9,1,6,12,52]

#Exercise 2


from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1
    print(nb_mystere)

    while nb_mystere != nb_test and compteur < 10:
        compteur += 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre etait ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre etait ", nb_mystere)


plus_ou_moins()