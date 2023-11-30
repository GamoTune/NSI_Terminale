def liste_puissances(a: int, n: int) -> list:
    if n < 1:
        return []

    l = [a] * n
    for i in range(1, n):
        for j in range(i):
            l[i] *= a
    return l

def liste_puissances_borne(a : int, borne : int) -> list:
    l = []
    if a >= 2:
        i = 0
        puissances = liste_puissances(a, borne)
        while puissances[i] < borne:
            l.append(puissances[i])
            i += 1
    return l


print("La liste des 0 puissances de 3",liste_puissances(3, 0))
print("La liste des 5 puissances de 3",liste_puissances(3, 5))
print("La liste des 4 puissances de 3",liste_puissances(-2, 4))
print("La liste des 3 puissances au bornes de 2",liste_puissances_borne(2, 3))
print("La liste des 2 puissances au bornes de 1",liste_puissances_borne(1, 2))
print("La liste des 16 puissances au bornes de 2",liste_puissances_borne(2, 16))
print("La liste des 17 puissances au bornes de 2",liste_puissances_borne(2, 17) )
print("La liste des 5 puissances au bornes de 5",liste_puissances_borne(5, 5))


assert liste_puissances(3, 0) == []
assert liste_puissances(3, 5) == [3, 9, 27, 81, 243]
assert liste_puissances(-2, 4) == [-2, 4, -8, 16]

assert liste_puissances_borne(2, 3) == [2]
assert liste_puissances_borne(1, 2) == []
assert liste_puissances_borne(2, 16) == [2, 4, 8]
assert liste_puissances_borne(2, 17) == [2, 4, 8, 16]
assert liste_puissances_borne(5, 5) == []


dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}

def est_parfait(mot):
    # mot est une chaîne de caractères (en lettres majuscules)
    code_concatene = ""
    code_additionne = 0
    for c in mot:
        code_concatene = code_concatene + str(dico[c])
        code_additionne = code_additionne + dico[c]
    code_concatene = int(code_concatene)
    if code_concatene % code_additionne == 0 :
        mot_est_parfait = True
    else:
        mot_est_parfait = False
    return code_additionne, code_concatene, mot_est_parfait

print("Le mot PAUL est-il parfait ?",est_parfait("PAUL")[2])
print("Le mot ALAIN est-il parfait ?",est_parfait("ALAIN")[2])


assert est_parfait("PAUL") == (50, 1612112, False)
assert est_parfait("ALAIN") == (37, 1121914, True)
