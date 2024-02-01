#Exercice N°1

def delta(tab) :
    tableau = []
    for i in range(len(tab)) :
        if i == 0 :
            tableau.append(tab[i])
        else :
            tableau.append(tab[i] - tab[i-1])
            
    return tableau
    

print("Le delta de : [1000, 800, 802, 1000, 1003] donne : ", delta([1000, 800, 802, 1000, 1003]))
print("Le delta de : [42] donne : ", delta([42]))

assert delta([1000, 800, 802, 1000, 1003]) == [1000, -200, 2, 198, 3]
assert delta([42]) == [42]


print()


#Exercice N°2

class Noeud:
    '''
    classe implémentant un noeud d'arbre binaire
    '''

    def __init__(self, g, v, d):
        '''
        un objet Noeud possède 3 attributs :
        - gauche : le sous-arbre gauche,
        - valeur : la valeur de l'étiquette,
        - droit : le sous-arbre droit.
        '''
        self.gauche = g
        self.valeur = v
        self.droit = d

    def __str__(self):
        '''
        renvoie la représentation du noeud en chaine de caractères
        '''
        return str(self.valeur)

    def est_une_feuille(self):
        '''
        renvoie True si et seulement si le noeud est une feuille
        '''
        return self.gauche is None and self.droit is None


def expression_infixe(e):
    s = ''
    if e.gauche is not None:
        s = '(' + s + expression_infixe(e.gauche) + ')'
    s = s + str(e.valeur)
    if e.droit is not None:
        s = s + '(' + expression_infixe(e.droit) + ')'
    return s


e = Noeud(Noeud(Noeud(None, 3, None),
    '*', Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))),
    '-', Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None)))
print("l'expression infixe de 'e' donne : ", expression_infixe(e))
assert expression_infixe(e) == "((3)*((8)+(7)))-((2)+(1))"