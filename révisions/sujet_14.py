#Exercice 1

def min_et_max(tab):
    min_max = {
        "min": tab[0],
        "max": tab[1]
    }
    for i in tab:
        if i < min_max["min"]:
            min_max["min"] = i
        elif i > min_max["max"]:
            min_max["max"] = i
    return min_max

print(min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))


#Exercice 2

class Carte:
    def __init__(self, c, v):
        """ Initialise les attributs couleur (entre 1 et 4), et valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v

    def recuperer_valeur(self):
        """ Renvoie la valeur de la carte : As, 2, ..., 10, Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def recuperer_couleur(self):
        """ Renvoie la couleur de la carte (parmi pique, coeur, carreau, trèfle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52 objets Carte possibles
            rangés par valeurs croissantes en commençant par pique, puis coeur,
            carreau et tréfle. """
        self.cartes = []
        for i in range(1, 5):
            for j in range(1, 14):
                self.cartes.append(Carte(i, j))

    def recuperer_carte(self, pos):
        """ Renvoie la carte qui se trouve à la position pos (entier compris entre 0 et 51). """
        assert 0 <= pos <= 51, "Ta mere la pute"
        return self.cartes[pos]