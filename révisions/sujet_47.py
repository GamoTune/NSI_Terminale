#Exercice 1

def max_dico(dico):
    max_key = ""
    max_value = 0
    for i in dico:
        if dico[i] > max_value:
            max_value = dico[i]
            max_key = i
    return (max_key, max_value)

print(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))


#Exercice 2

class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie le booléen True si la pile est vide, False sinon."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l’élément placé au sommet de la pile,
        si la pile n’est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()


def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != '+' and element != '*':
            p.empiler(element)
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return p.depiler()

print(eval_expression([2, 3, '+', 5, '*']))