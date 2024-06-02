#Exercice 1

def recherche(tab, n):
    debut = 0
    fin = len(tab)-1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if tab[milieu] == n:
            return milieu
        elif tab[milieu] <= n:
            debut = milieu+1
        else:
            fin = milieu-1
    return None


#Exercice 2

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    '''Renvoie le message codé par la méthode de César
    pour le decalage donné'''
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c)+decalage) % 26 
            resultat = resultat + alphabet[indice]
        else:
            resultat += c
    return resultat

print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4))
