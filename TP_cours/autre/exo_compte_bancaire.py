class CompteBancaire:
    def __init__(self,nom) -> None:
        self.nom = nom
        self.solde = 0
    
    def get_nom(self):
        return f"{self.nom}"

    def get_solde(self):
        return f"{self.solde}"
    
    def __str__(self) -> str:
        return f"{self.nom, self.solde}"
    
    def _set_solde(self, variation):
        if variation <= 0 and self.solde < variation:
            return "ATTENTION vous ne pouvez pas faire un retrait d'un montent supérieur au solde de votre compte"
        else:
            self.solde += variation
            return f"Votre nouveau solde est de : {self.solde}"
        
    def depot(self, variation):
        if variation <= 0:
            variation += 2*variation
        self.set_solde(variation)

    def retrait(self, variation):
        if variation >= 0:
            variation -= 2*variation
        self.set_solde(variation)
    
    def affichage(self):
        return f"Le copte bancaire appartient à : {self.nom} \nLe solde est de : {self.solde}€"
