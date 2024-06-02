#Exercice 1

def moyenne(notes):
    resultat = 0
    numerateur = 0
    denominateur = 0
    for i in range(len(notes)):
        numerateur += (notes[i][0]*notes[i][1])
        denominateur += notes[i][1]
    return numerateur/denominateur

print(moyenne([(15.0,2),(9.0,1),(12.0,3)]))


#Exercice 2

def ligne_suivante(ligne):
    '''Renvoie la ligne suivant ligne du triangle de Pascal'''
    ligne_suiv = [ligne[0]]
    for i in range(1, len(ligne)):
        ligne_suiv.append(ligne[i-1] + ligne[i])
    ligne_suiv.append(ligne[0])
    return ligne_suiv

def pascal(n):
    '''Renvoie le triangle de Pascal de hauteur n'''
    triangle = [ [1] ]
    for k in range(n):
        ligne_k = ligne_suivante(triangle[k])
        triangle.append(ligne_k)
    return triangle

print(ligne_suivante([1, 3, 3, 1]))
print(pascal(2))