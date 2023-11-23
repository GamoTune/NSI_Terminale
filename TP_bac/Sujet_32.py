
#Exo 1
def min_et_max(tab):
    """Renvoie un dictionnaire contenant le minimum et le maximum du tableau tab"""
    assert len(tab) > 0, "tableau vide"
    mini = tab[0]
    maxi = tab[0]
    for v in tab:
        if v > maxi:
            maxi = v
        if v < mini:
            mini = v
    return {'min':mini, 'max': maxi}

print("Le minimum et le maximum dans la liste [0, 1, 4, 2, -2, 9, 3, 1, 7, 1] est : ",min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))
print("Le minimum et le maximum dans la liste [0, 1, 2, 3] est : ",min_et_max([0, 1, 2, 3]))
print("Le minimum et le maximum dans la liste [3] est : ",min_et_max([3]))
print("Le minimum et le maximum dans la liste [1, 3, 2, 1, 3] est : ",min_et_max([1, 3, 2, 1, 3]))
print("Le minimum et le maximum dans la liste [-1, -1, -1, -1, -1] est : ",min_et_max([-1, -1, -1, -1, -1]))
assert min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}
assert min_et_max([0, 1, 2, 3]) == {'min': 0, 'max': 3}
assert min_et_max([3]) == {'min': 3, 'max': 3}
assert min_et_max([1, 3, 2, 1, 3]) == {'min': 1, 'max': 3}
assert min_et_max([-1, -1, -1, -1, -1]) == {'min': -1, 'max': -1}

#Exo 2
class Carte:
    def __init__(self, c, v):
        self.couleur = c
        self.valeur = v

    def get_valeur(self):
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def get_couleur(self):
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        self.paquet=[]
        for c in range (1,5):
            for v in range(1,14):
                self.paquet.append(Carte(c,v))
            

    def get_carte(self, pos):
        assert pos < 52 and pos > -1, "paramètre pos invalide"
        return self.paquet[pos]

jeu = Paquet_de_cartes()
carte1 = jeu.get_carte(20)
print("La carte 1 est un " + carte1.get_valeur() + " de " + carte1.get_couleur())

carte2 = jeu.get_carte(0)
print("La carte 2 est un " + carte2.get_valeur() + " de " + carte2.get_couleur())

carte3 = jeu.get_carte(52)





