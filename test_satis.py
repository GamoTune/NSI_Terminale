class Plaque_fer():
    def __init__(self) -> None:
        self.nbr_constructeur = 0
        self.nbr_plaque = 0

    def plaque_fer(self, fer):
        self.nbr_constructeur = fer/30
        self.nbr_plaque = self.nbr_constructeur*20
        return self.nbr_plaque

class Tige_fer():
    def __init__(self) -> None:
        self.nbr_constructeur = 0
        self.nbr_tige = 0

    def tige_fer(self, fer):
        self.nbr_constructeur = fer/15
        self.nbr_tige = self.nbr_constructeur*15
        return self.nbr_tige

def calcul_satis(fer):
    plaque = Plaque_fer()
    tige = Tige_fer()
    return plaque.plaque_fer(fer/2),tige.tige_fer(fer/2)

plaque = Plaque_fer()
tige = Tige_fer()
print(plaque.plaque_fer(120))
print(tige.tige_fer(120))
print(calcul_satis(120))
