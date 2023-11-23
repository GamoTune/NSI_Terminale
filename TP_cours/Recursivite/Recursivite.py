def premierExempleRecursif(nbreBoucle):
    if nbreBoucle > 9:
        print("Fin de la récursivité")
    else:
        print("Début de la récursivité")
        print("nbreBoucle = ", nbreBoucle)
        nbreBoucle += 1
        premierExempleRecursif(nbreBoucle)
premierExempleRecursif(1)




def puissance(x, n):
    if n == 0:
        return 1
    else:
        return x * puissance(x, n-1)
print(puissance(2, 3))

print()


"""def puissance_recursive(nbre, puis):
    if puis == 0:
        return 1
    else:
        return nbre * puissance_recursive(nbre, puis-1)



print("Ce programme calcule la puissance d'un nombre sans utiliser l'opérateur **")
nbr = float(input("Veuillez saisir le nombre : "))
puiss = float(input("Veuillez saisir la puissance : "))
print("Le nombre {} à la puissance {} est égal à {}".format(nbr, puiss, puissance_recursive(nbr, puiss)))
"""
print()


def compte_a_rebours(n):
    if n == 0:
        print("Fin du compte à rebours")
    else:
        print(n)
        compte_a_rebours(n-1)

compte_a_rebours(10)

print()


def som_n_prem_entiers(nbr):
    if nbr == 1:
        return 1
    else:
        return nbr + som_n_prem_entiers(nbr-1)

print(som_n_prem_entiers(5))


def binaire(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * binaire(n // 2)

print(binaire(10))

print()


def palindrome(chaine):
    if len(chaine) <= 1:
        return True
    else:
        return chaine[0] == chaine[-1] and palindrome(chaine[1:-1])

print(palindrome("kayak"))

print()

#Fonction récurssive qui renverse une chaine de caractère
def renverse(chaine):
    if len(chaine) <= 1:
        return chaine
    else:
        return renverse(chaine[1:]) + chaine[0]

print(renverse("sucé ses écus"))

print()


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(10))

print()

