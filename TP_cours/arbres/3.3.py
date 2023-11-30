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




from queue import Queue 
def BFS(arbre):
  file = Queue()
  file.put(arbre)
  resultat = []
  while file.empty() is False :
    element = file.get()
    if element is not None :
      print("L'arbre ou le sous arbre est : ",element) 
      resultat.append(element.get_racine())
      print(resultat)
      file.put(element.get_gauche())
      file.put(element.get_droite())
  return resultat

print("---------- C'est la BFS (Breadth First Search), parcours en largeur d’abord ----------") 
print("Le parcours en largeur d’abord de l'arbre donne la liste suivante : ",BFS(arbr))






def prefixe(arbre):
    resultat = []
    resultat.append(arbre._racine)
    if arbre._gauche is not None:
        resultat.append(prefixe(arbre._gauche))
    if arbre._droite is not None:
        resultat.append(prefixe(arbre._droite))
    return resultat

def taille(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + taille(arbre._gauche) + taille(arbre._droite)

def hauteur(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + max(hauteur(arbre._gauche), hauteur(arbre._droite))

def infixe(arbre):
    resultat = []
    if arbre._gauche is not None:
        resultat.append(infixe(arbre._gauche))
    resultat.append(arbre._racine)
    if arbre._droite is not None:
        resultat.append(infixe(arbre._droite))
    return resultat


def aplatirListe(liste):
    for element in liste:
        if type(element) == list:
            aplatirListe(element)
        else:
            listePlate.append(element)
    return listePlate

print("---------- C'est la DFS (Depth First Search), parcours préfixe en profondeur d’abord ----------")
print("Le parcours préfixe en profondeur de l'arbre donne la liste suivante : ",prefixe(arbr))
listePlate = []
print("Le parcours préfixe en profondeur de l'arbre donne la liste aplatie suivante : ",aplatirListe(prefixe(arbr))) 

def recherche(arbre, valeur):
    if arbre._racine == valeur:
        return True
    if arbre._gauche is not None:
        if recherche(arbre._gauche, valeur):
            return True
    if arbre._droite is not None:
        if recherche(arbre._droite, valeur):
            return True
    return False

print("---------- C'est la recherche d'une valeur dans l'arbre ----------")
for val in range(0,21):
    print("La clé",val,"est dans l'arbre : ",recherche(arbr,val)) 


# ---------------------------- Exercice 4 ----------------------------


def aplatirListe2(liste, listePlateParcoursInfixe):
    for element in liste:
        if type(element) == list:
            aplatirListe2(element, listePlateParcoursInfixe)
        else:
            listePlateParcoursInfixe.append(element)
    return listePlateParcoursInfixe

def est_arb(arbre, list):
    list = aplatirListe2(infixe(arbre), list)
    for i in range(0, len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

