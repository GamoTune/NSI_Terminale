#Exercice 1

def moyenne(tab):
    if len(tab):
        x = 0
        for i in tab:
            x += i
        zMoyenne = x/len(tab)
        return zMoyenne
    else:
        return "La moyenne ne peut pas être efectué car le tableau est vide"



aaaaa = [0,1,2,3,4,5,6,7,8,9,10]

print("La moyenne de aaaaa", moyenne(aaaaa))

##########################################################################################

#Exercice 2

def tri(tab):
    # i est le premier indice de la zone non triée,
    # j est le dernier indice de cette zone non triée.
    # Au début, la zone non triée est le tableau complet.
    i= 0
    j= len(tab)-1
    while i != j :
        if tab[i] == 0:
            i += 1
        else :
            tab[i], tab[j] = tab[j], tab[i]
            j -= 1
    return tab

print(tri([0, 1, 0, 1, 0, 1, 0, 1, 0]))
