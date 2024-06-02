#Exercice 1

class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit

a = Noeud(1, Noeud(4, None, None), Noeud(0, None, Noeud(7, None, None)))



def taille(a):
    if a == None:
        return 0
    return taille(a.gauche) + taille(a.droit) + 1

print(taille(a))

def hauteur(a):
    if a == None:
        return -1
    return max(hauteur(a.gauche), hauteur(a.droit)) + 1

print(hauteur(a))


#Exercice 2

def ajoute(indice, element, tab):
    '''Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = tab[i] 
    tab_ins[indice] = element 
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = tab[i-1]
    return tab_ins

print(ajoute(0, 4, [7, 8, 9]))