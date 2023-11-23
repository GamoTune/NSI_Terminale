#Exercise 1
def nbr_occurrences(chaine):
    """
    :param chaine: str
    :return: dict
    """
    dico = {}
    for c in chaine:
        if c in dico:
            dico[c] += 1
        else:
            dico[c] = 1
    return dico

chn = "abcdd"
print(f"le nombre d'occurrences de chaque caratères est : {nbr_occurrences(chn)}")
assert nbr_occurrences("abcd") == {'a': 1, 'b': 1, 'c': 1, 'd': 1}



#Exercice 2
def fusion(lst1, lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    lst12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2 :
        if lst1[i1] < lst2[i2]:
            lst12[i] = lst1[i1]
            i1 = i1 + 1
        else:
            lst12[i] = lst2[i2]
            i2 = i2 + 1
        i += 1
    while i1 < n1:
        lst12[i] = lst1[i1]
        i1 = i1 + 1
        i = i + 1
    while i2 < n2:
        lst12[i] = lst2[i2]
        i2 = i2 + 1
        i = i + 1
    return lst12


print(f"la fusion des liste [1,6,10] et [0, 7, 8, 9] est : {fusion([1, 6, 10], [0, 2, 7, 8, 9])}")
assert fusion([1, 6, 10], [0, 7, 8, 9]) == [0, 1, 6, 7, 8, 9, 10]
