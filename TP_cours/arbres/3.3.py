class Arbre: # Arbre binaire en POO
    def __init__(self,valeur):
        self._racine = valeur
        self._gauche = None
        self._droite = None
    def set_gauche(self, sousarbre):
        self._gauche = sousarbre
    def set_droite(self, sousarbre):
        self._droite = sousarbre
    def get_gauche(self):
        """Renvoie le sous-arbre gauche de l'arbre self."""
        return self._gauche
    def get_droite(self):
        """Renvoie le sous-arbre droit de l'arbre self."""
        return self._droite
    def get_racine(self):
        """Renvoie la racine de l'arbre self."""
        return self._racine
    def __str__(self):
        return "({},{},{})".format(self._gauche, self._racine, self._droite)
arbr = Arbre(4)
print(arbr)
arbr.set_gauche(Arbre(3))
print(arbr)
arbr.set_droite(Arbre(1))
print(arbr)
arbr.get_droite().set_gauche(Arbre(2))
print(arbr)
arbr.get_droite().set_droite(Arbre(7))
print(arbr)
arbr.get_gauche().set_gauche(Arbre(6))
print(arbr)
arbr.get_droite().get_droite().set_gauche(Arbre(9))
print(arbr)
print("La racine du sag du sad de l'arbre est : ",arbr.get_droite().get_gauche().get_racine())
print("La racine du sag du sad de l'arbre est : ",arbr.get_gauche().get_gauche().get_racine())
print("La racine du sag du sad de l'arbre est : ",arbr.get_droite().get_droite().get_gauche().get_racine()) 