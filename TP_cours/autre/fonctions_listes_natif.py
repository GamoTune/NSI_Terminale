def nouvelleList():
    return []

def estVide(lst):
    if len(lst):
        print("Attention la liste est vide")
        return False
    return True

def compteListe(lst):
    return len(lst)

def afficherListe(lst):
    return str(lst)

def lireElement(lst, position):
    if position < len(lst):
        return lst[position]
    else: return "l'index n'existe pas"


