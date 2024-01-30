def ajoute_dictionnaires(d1,d2):
    d = {}
    for key in d1.keys():
        d[key] = d1[key]
    for key in d2.keys():
        if key in d:
            d[key] += d2[key]
        else:
            d[key] = d2[key]
    return d

print("L'ajout de {1: 5, 2: 7} dans {2: 9, 3: 11} donne : ", ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))
print("L'ajout de {} dans {2: 9, 3: 11} donne : ", ajoute_dictionnaires({}, {2: 9, 3: 11}))
print("L'ajout de {1: 5, 2: 7} dans {} donne : ", ajoute_dictionnaires({1: 5, 2: 7}, {}))

assert ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}) == {1: 5, 2: 16, 3: 11}
assert ajoute_dictionnaires({}, {2: 9, 3: 11}) == {2: 9, 3: 11}
assert ajoute_dictionnaires({1: 5, 2: 7}, {}) == {1: 5, 2: 7}

print("-----------------------------------------------------------------------------------------")


from random import randint

def nbre_coups():
    n = 0
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < 12:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % nbre_cases
        if case_en_cours not in cases_vues:
            cases_vues.append(case_en_cours)
        n += 1
    return n,cases_vues

a = nbre_coups()
print("Le nombre de coups nécessaires pour faire 12 case est : ", a[0], ". L'ordre des case obtenu est : ", a[1])
