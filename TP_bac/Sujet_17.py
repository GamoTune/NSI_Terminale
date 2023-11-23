#Exercice 1

def moyenne(liste_notes):
    x = 0
    y = 0
    for i in liste_notes:
        x += i[0]*i[1]
        y += i[1]
    return x/y


###############################################################################################

#Exercice 2

def pascal(n):
    triangle= [[1]]
    for k in range(1,n):
        ligne_k = [1]
        for i in range(1,k):
            ligne_k.append(triangle[k-1][i-1]+triangle[k-1][i])
        ligne_k.append(1)
        triangle.append(ligne_k)
    return triangle




print("La moyenne de la liste ([(15, 2), (9, 1), (12, 3)]) est : ",moyenne(([(15, 2),(9, 1),(12, 3)])))

print("Le triangle de Pascal pour 5 : ",pascal(5))