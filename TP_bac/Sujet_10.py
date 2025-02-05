#Exo 1

def maxliste(tab):
    max = tab[0]
    for i in tab:
        if i > max:
            max = i

    return max

print("Le maximum dans la liste [98, 12, 104, 23, 131, 9] est : ", maxliste([98, 12, 104, 23, 131, 9]))
print("Le maximum dans la liste [-27, 24, -3, 15] est : ", maxliste([-27, 24, -3, 15]))



#Exo 2

class Pile:
    """
    Classe définissant une pile
    """
    def __init__(self):
        self.valeurs = []

    def est_vide(self):
        """
        Renvoie True si la pile est vide, False sinon
        """
        return self.valeurs == []

    def empiler(self, c):
        """
        Place l’élément c au sommet de la pile
        """
        self.valeurs.append(c)

    def depiler(self):
        """
        Supprime l’élément placé au sommet de la pile, à
        condition
        qu’elle soit non vide
        """
        if self.est_vide() == False:
            self.valeurs.pop()



def parenthesage(ch):
    """
    Renvoie True si la chaîne ch est bien parenthésée
    et False sinon
    """
    p = Pile()
    for c in ch:
        if c == "(":
            p.empiler(c)
        elif c == ")":
            if p.est_vide():
                return False
            else:
                p.depiler()
    return p.est_vide()
print()
print("Le parenthesage de '((()())(()))' est : ", parenthesage("((()())(()))"))

print("Le parenthesage de '((()())()))' est : ", parenthesage("((()())()))"))