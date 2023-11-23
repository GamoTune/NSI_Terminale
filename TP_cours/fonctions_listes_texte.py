def nouvelleListe(): #Retourne une lsite vide
    return []

def estVide(lst): #Teste si la liste est vide ou non
    if len(lst):
        return False
    return True

def insererTete(x, lst): #Fonction insert
    lst2 = x
    for i in range(len(lst)):
        lst2.append(lst[i])
    return lst2

def lireTete(lst): #Lire la tête de la liste
    if len(lst) >= 1:
        return lst[0]

def supprimerTete(lst):
    if len(lst) < 1:
        return []
    else:
        lst2 = []
        for i in range(1, len(lst)):
            lst2.append(lst[i])
        return lst2



print(supprimerTete([0,1,2,3,4,5,6,7,8,9]))