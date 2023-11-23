def pile():
    return []

def vide(p):
    return bool(p)

def empiler(p,x):
    p.append(x)

def depiler(p):
    try:
        return p.pop()
    except:
        print("attention votre pile est vide")
        return None

def taille(p):
    if vide(p):
        return "La liste est vide"
    else:
        return len(p)

def sommet(p):
    if vide(p):
        return "La liste est vide"
    else:
        return p[-1]
    
