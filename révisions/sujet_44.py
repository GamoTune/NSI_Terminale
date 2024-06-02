#Exercice 1

def enumere(tab):
    d = {}
    for i in range(len(tab)):
        if tab[i] in d.keys():
            d[tab[i]].append(i)
        else:
            d[tab[i]] = [i]
    return d


print(enumere([1, 1, 2, 3, 2, 1]))


#Exercice 2

class Noeud:
    """Classe représentant un noeud d'un arbre binaire"""
    def __init__(self, etiquette, gauche, droit):
        """Crée un noeud de valeur etiquette avec 
        gauche et droit comme fils."""
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit

def parcours(arbre, liste):
    """parcours récursivement l'arbre en ajoutant les étiquettes
    de ses noeuds à la liste passée en argument en ordre infixe."""
    if arbre != None:
        parcours(arbre.gauche, liste)
        liste.append(arbre.etiquette)
        parcours(arbre.droit, liste)
    return liste


def insere(arbre, cle):
    """insere la cle dans l'arbre binaire de recherche
    représenté par arbre.
    Retourne l'arbre modifié."""
    if arbre == None:
        return Noeud(cle, None, None) # creation d'une feuille
    else:
        if cle < arbre.etiquette:
            arbre.gauche = insere(arbre.gauche, cle)
        else:
            arbre.droit = insere(arbre.droit, cle)
        return arbre
    
a = insere(None, 1)
print(a.gauche, a.etiquette, a.droit)
a = insere(a, 4)
print(a.gauche, a.etiquette, a.droit)