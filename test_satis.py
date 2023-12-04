class Plaque_fer():
    def __init__(self) -> None:
        self.nbr_constructeur = 0
        self.nbr_plaque = 0

    def plaque_fer(self, fer):
        self.nbr_constructeur = fer/30
        self.nbr_plaque = self.nbr_constructeur*20
        return self.nbr_plaque
    
    def plaque_plastique(self, fer, plastique):
        pass 

plaque = Plaque_fer()
print(plaque.plaque_fer(120))
print(plaque.plaque_plastique(10,20))