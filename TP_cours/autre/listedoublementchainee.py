class Maillon:

    def __init__(self, valeur) -> None:
        self.valeur = valeur
        self.precedent = None
        self.suivant = None


class File:
    def __init__(self) -> None:
        self.longueur = 0
        self.debut = None
        self.fin = None

    def enfiler(self, el):
        nouveau_maillon = Maillon(el)
        if self.vide():
            self.debut = nouveau_maillon
            self.fin = nouveau_maillon
        else:
            self.fin.suivant = nouveau_maillon
            nouveau_maillon.precedent = self.fin
            self.fin = nouveau_maillon
        self.longueur += 1

    def vide(self):
        return self.longueur == 0
    
    def defiler(self):
        if not self.vide():
            valeur_defilee = self.debut.valeur
            self.debut = self.debut.suivant
            if self.debut:
                self.debut.precedent = None
            else:
                self.fin = None
            self.longueur -= 1
            return valeur_defilee
        else:
            return Exception("La file est vide")
            
        
    def __str__(self) -> str:
        elements = []
        current = self.debut
        while current:
            elements.append(current.valeur)
            current = current.suivant
        return "Etat de la file: " + ", ".join(elements)