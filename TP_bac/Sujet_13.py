#Exercise 1

def recherche(a: float, tab:list) -> int: # tab est une liste d'entiers
    x = 0 # nombre d'occurences de a dans tab
    for i in range(len(tab)): # pour chaque élément de tab
        if tab[i] == a: # si l'élément est égal à a
            x += 1 # on incrémente x
    return x # on renvoie x


print("le nombre de fois que la valeur '5' est trouvé est : ",recherche(5, []))
print("le nombre de fois que la valeur '5' est trouvé est : ",recherche(5, [-2, 3, 4, 8]))
print("le nombre de fois que la valeur '5' est trouvé est : ",recherche(5, [-2, 3, 1, 5, 3, 7, 4]))
print("le nombre de fois que la valeur '5' est trouvé est : ",recherche(5, [-2, 5, 3, 5, 4, 5]))




#Exercice 2

pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee): # somme_due <= somme_versee

    rendu = [] # liste des pièces à rendre
    a_rendre = somme_versee - somme_due # somme à rendre
    i = len(pieces) - 1 # indice de la plus grande pièce
    while a_rendre > 0 : # tant qu'il reste de l'argent à rendre
        if pieces[i] <= a_rendre : # si la pièce est inférieure à la somme à rendre
            rendu.append(pieces[i]) # on ajoute la pièce à la liste des pièces à rendre
            a_rendre = a_rendre - pieces[i] # on retire la pièce de la somme à rendre
        else : # si la pièce est supérieure à la somme à rendre
            i = i - 1 # on passe à la pièce inférieure
    return rendu # on renvoie la liste des pièces à rendre

print(rendu_monnaie(102, 500))