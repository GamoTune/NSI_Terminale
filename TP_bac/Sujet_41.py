#Execice 1

def recherche(caractere, chaine):
    nbr_i = 0
    for i in chaine:
        if caractere == i:
            nbr_i += 1
    return nbr_i

print(recherche('b', "zimbabwé"))

print()


valeurs = [100,50,20,10,5,2,1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre :
        return [v] + rendu_glouton(a_rendre - v, rang)
    else :
        return rendu_glouton(a_rendre, rang+1)

print(rendu_glouton(291, 1))