#Exercise 1

def moyenne(lst):
    coefs = 0
    vals = 0
    for tup in lst:
        vals += tup[0]*tup[1]
        coefs += tup[1]
    if coefs == 0:
        return None
    else:
        return vals/coefs
    
print("La moyenne de la liste [(8, 2), (12, 0), (13.5, 1), (5, 0.5)] est : ", moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))
print("La moyenne de la liste [(3, 0), (5, 0)] est : ", moyenne([(3, 0), (5, 0)]))


#Exercice 2

coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par
        des " *" , les 0 par deux espaces "  " 
        La valeur "" donnée au paramètre end permet 
        de ne pas avoir de  saut de ligne. '''
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *", end="")
            else:
                print("  ", end="")
        print()


def zoomListe(liste_depart, k):
    '''renvoie une liste contenant k fois chaque
       élément de liste_depart'''
    liste_zoom = []
    for elt in liste_depart :
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom

def zoomDessin(grille, k):
    '''renvoie une grille ou les lignes sont zoomées k fois
       ET répétées k fois'''
    grille_zoom=[]
    for elt in grille:
        liste_zoom = zoomListe(elt, k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom


affiche(coeur)
affiche(zoomDessin(coeur, 3))

trad_linguistique = moyenne([(17, 7), (6, 7)])
print(moyenne([(trad_linguistique, 7), (7, 4), (10, 4), (11, 7), (16, 3), (10, 3), (10, 2)]))

#Trad : 17, 7
#Linguistique : 6, 7
#Civilisation GB, US : 7, 4
#Histoire de l'art, Textes et images : 10, 4
#Litérature : 11, 7
#Comprehension oral : 16, 3
#Civilisation de l'antiquité : 10, 3
#Pix : 10, 2