#Exo 1

#Question 7

def recherche_nom(dic):
    noms = {}
    for i in range(len(dic)):
        nom = dic[i]['nom']
        if nom in noms: noms[nom] += 1
        else: noms[nom] = 1
    new_noms = []
    for j in noms.keys():
        if noms[j] >= 0:
            new_noms.append(j)
    return new_noms


a = [{'idmus': 12, 'nom': 'Parker', 'prenom': 'Charlie',
'instru': 'trompette', 'idgrp' : 96, 'nb_concerts': 5},
{'idmus': 13, 'nom': 'Parker', 'prenom': 'Charlie',
'instru': 'trombone', 'idgrp' : 25, 'nb_concerts': 9},
{'idmus': 58, 'nom': 'Dufler', 'prenom': 'Candy',
'instru': 'saxophone', 'idgrp' : 96, 'nb_concerts': 4},
{'idmus': 97, 'nom': 'Miles', 'prenom': 'Davis',
'instru': 'saxophone', 'idgrp' : 87, 'nb_concerts': 2},
]
print(recherche_nom(a))