#Exercice 1

def recherche_indice_classement(element, liste): # fonction qui renvoie l'indice de l'élément dans la liste
    lst1 = []
    lst2 = []
    lst3 = []
    for i in range(len(liste)): # on parcourt la liste
        if liste[i] < element: # si l'élément est inférieur à l'élément recherché
            lst1.append(i) # on ajoute l'indice à la liste 1
        elif liste[i] == element: # si l'élément est égale à l'élément recherché
            lst2.append(i) # on ajoute l'indice à la liste 2
        else: # si l'élément est supérieur à l'élément recherché
            lst3.append(i) # on ajoute l'indice à la liste 3
    return lst1, lst2, lst3 # on renvoie les 3 listes

print("Les indice des valeurs inferieur, eguale, et superieur a 3 sont : ", recherche_indice_classement(3, [1,3,4,2,4,6,3,0])) # on teste la fonction
print("Les indice des valeurs inferieur, eguale, et superieur a 3 sont : ", recherche_indice_classement(3, [1,4,2,4,6,0])) # on teste la fonction
print("Les indice des valeurs inferieur, eguale, et superieur a 3 sont : ", recherche_indice_classement(3, [1,1,1,1])) # on teste la fonction
print("Les indice des valeurs inferieur, eguale, et superieur a 3 sont : ", recherche_indice_classement(3, [])) # on teste la fonction

assert recherche_indice_classement(3, [1,3,4,2,4,6,3,0]) == ([0,3,7], [1,6], [2,4,5]) # on teste la fonction

assert recherche_indice_classement(3, [1,3,4,2,4,6,3,0]) == ([0,3,7], [1,6], [2,4,5])
assert recherche_indice_classement(3, [1,4,2,4,6,0]) == ([0,2,5], [], [1,3,4])
assert recherche_indice_classement(3, [1,1,1,1]) == ([0,1,2,3], [], [])
assert recherche_indice_classement(3, []) == ([], [], [])


#Exercice 2

resultats = {'Dupont': {
                        'DS1': [15.5, 4],
                        'DM1' : [14.5, 1],
                        'DS2': [13, 4],
                        'PROJET1' : [16, 3],
                        'DS3': [14, 4]
                        },
            'Durand': {
                        'DS1': [6, 4],
                        'DM1' : [14.5, 1],
                        'DS2': [8, 4],
                        'PROJET1' : [9, 3],
                        'IE1' : [7, 2],
                        'DS3': [8, 4],
                        'DS4': [15, 4]
                    }
            }

def moyenne(nom, dico_result): # fonction qui renvoie la moyenne d'un élève
    if nom in dico_result: # si le nom est dans le dictionnaire
        notes = dico_result[nom] # on récupère les notes
        total_points = 0 # on initialise le total des points
        total_coeffiecients = 0 # on initialise le total des coefficients
        for valeurs in notes.values(): # on parcourt les valeurs
            note, coefficient = valeurs # on récupère la note et le coefficient
            total_points += note * coefficient # on ajoute la note multiplié par le coefficient au total des points
            total_coeffiecients += coefficient # on ajoute le coefficient au total des coefficients
        return round(total_points / total_coeffiecients, 1) # on renvoie la moyenne
    else: # si le nom n'est pas dans le dictionnaire
        return -1 # on renvoie -1


print("La moyenne de Dupont est : ", moyenne("Dupont", resultats))
print("La moyenne de Durand est : ", moyenne("Durand", resultats))

assert moyenne("Dupont", resultats) == 14.5
assert moyenne("Durand", resultats) == 9.2