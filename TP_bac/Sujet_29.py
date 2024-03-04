#Exercice 1

print("Exercice 1")
class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def taille(a):
    if a == None:
        return 0
    else:
        return 1 + taille(a.fg) + taille(a.fd)

def hauteur(a):
    if a == None:
        return 0
    else:
        return 1 + max(hauteur(a.fg), hauteur(a.fd))

a = Arbre(0)
a.fg = Arbre(1)
a.fg.fg = Arbre(3)
a.fd = Arbre(2)
a.fd.fg = Arbre(4)
a.fd.fd = Arbre(6)
a.fd.fd = Arbre(5)

print("La taille de a est : ", taille(a))
print("La hauteur de a est : ", hauteur(a))

print()
print("-----------------------------")
print()

#Exercice 2

print("Exercice 2")
def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)]
    if indice < nbre_elts:
        for i in range(indice):
            L[i] = liste[i]
        L[indice] = element
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = liste[i-1]
    else:
        for i in range(nbre_elts):
            L[i] = liste[i]
        L[-1] = element
    return L


print("L'ajout de 1 à la place 4 dans [7, 8, 9] donne : ", ajoute(1, 4, [7, 8, 9]))
print("L'ajout de 3 à la place 4 dans [7, 8, 9] donne : ", ajoute(3, 4, [7, 8, 9]))
print("L'ajout de 4 à la place 4 dans [7, 8, 9] donne : ", ajoute(4, 4, [7, 8, 9]))
