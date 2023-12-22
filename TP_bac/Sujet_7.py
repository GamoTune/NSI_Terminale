#Exercice 1

def fusion(tab1:list, tab2:list):
    lst = tab1+tab2
    lst.sort()
    return lst


print(fusion([3, 5], [2, 5]))
print(fusion([-2, 4], [-3, 5, 10]))
print( fusion([4], [2, 6]))


print()

romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre) :
    """ Renvoie l'ecriture decimale du nombre donné en chiffres romains """

    if len(nombre) == 1:
        return romains[nombre[0]]

    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]


print(traduire_romain("CXLII"))
