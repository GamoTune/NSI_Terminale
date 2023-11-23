#Exercice 1

def recherche(tab,n):
    if n in tab:
        return tab.index(n)
    return len(tab)


tableau1 = [5,3]
print(recherche(tableau1, 12))

##############################################################

#Exercice 2

from math import sqrt # import de la fonction racine carrée
def distance(point1, point2):
    """ Calcule et renvoie la distance entre deux points. """
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant à la plus
    courte distance du point depart."""
    point = tab[0]
    min_dist = distance(point, depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(point, depart)
    return point

assert distance((1,0),(5,3)) == 5.0
print(distance((1,0),(5,3)))
