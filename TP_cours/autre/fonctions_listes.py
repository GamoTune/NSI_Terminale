def lireElement(lst, position):
    if position < len(lst):
        return lst[position]
    return "La valeur n'exsite pas"


def insererElement(x, lst, position):
    if position <= len(lst):
        lst.insert(position, x)
        return lst
    return "La valeur n'exsite pas"

def supprimerElement(lst, position):
    if position < len(lst):
        del lst[position]
        return lst
    return "La valeur n'exsite pas"