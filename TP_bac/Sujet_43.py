#Exercice 1
#Écrire une fonction ecriture_binaire_entier_positif qui prend en paramètre un entier positif n et renvoie une liste d'entiers correspondant à l‘écriture binaire de n.
#Ne pas oublier d’ajouter au corps de la fonction une documentation et une ou plusieurs assertions pour vérifier les pré-conditions.

def ecriture_binaire_entier_positif(n):
    '''
    Renvoie la liste des bits de n
    '''
    assert n>=0, "n doit être positif"
    if n==0:
        return [0]
    else:
        return ecriture_binaire_entier_positif(n//2)+[n%2]


print(ecriture_binaire_entier_positif(2))





######################################################################
#Exercice 2

def tri_bulles(T):
    '''
    Trie T par ordre croissant
    '''
    n=len(T)-1
    for i in range(n):
        for j in range(n-i):
            if T[j]>T[j+1]:
                T[j],T[j+1]=T[j+1],T[j]
    return T