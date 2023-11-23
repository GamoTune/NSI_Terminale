#Exercice 1

def recherche(tab, element):
    for i in range(len(tab)):
        if tab[i] == element:
            return i
    return -1

print("La recherche de 5 dans [2, 3, 4, 5, 6], donne l'index : ", recherche([2, 3, 4, 5, 6], 5))
print("La recherche de 5 dans [2, 3, 4, 6, 7], donne l'index : ", recherche([2, 3, 4, 6, 7], 5))

print()



ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def position_alphabet(lettre):
    return ord(lettre) - ord('A')


def cesar(message, decalage):
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c) + decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + c
    return resultat


print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4))
print(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5))