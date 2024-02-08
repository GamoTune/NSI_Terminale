#Exercice N°1

def enumere(L):
    dico = {}
    i = 0
    for l in L:
        if l in dico:
            dico[l] = dico[l] + [i]
        else:
            dico[l] = [i]
        i += 1
    return dico

print("L'énumération de [1, 1, 2, 3, 2, 1] donne : ", enumere([1, 1, 2, 3, 2, 1]))

assert enumere([1, 1, 2, 3, 2, 1]) == {1: [0, 1, 5], 2: [2, 4], 3: [3]}

print()


#Exercice N°2
class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def parcours(arbre, liste):
    if arbre != None:
        parcours(arbre.fg, liste)
        liste.append(arbre.v)
        parcours(arbre.fd, liste)
    return liste

def insere(arbre, cle):
    """ arbre est une instance de la classe Arbre qui implémente
        un arbre binaire de recherche.
    """
    if cle < arbre.v:
        if arbre.fg is not None:
            insere(arbre.fg, cle)
        else:
            arbre.fg = Arbre(cle)
    else:
        if arbre.fd is not None:
            insere(arbre.fd, cle)
        else:
            arbre.fd = Arbre(cle)

a = Arbre(5)
insere(a, 2)
insere(a, 3)
insere(a, 7)
l = []

print("Le parcours de a dans 1 donne : ", parcours(a, l))
#assert parcours(a, l) == [2, 3, 5, 7]