#Exercice 1

def verifie(tab):
    for i in range(len(tab)-1):
        if tab[i] > tab[i+1]:
            return False
    return True

print("La liste [0, 5, 8, 8, 9] est trier dans l'ordre croissant : ", verifie([0, 5, 8, 8, 9]))
print("La liste [8, 12, 4] est trier dans l'ordre croissant : ", verifie([8, 12, 4]))
print("La liste [-1, 4] est trier dans l'ordre croissant : ", verifie([-1, 4]))
print("La liste [5] est trier dans l'ordre croissant : ", verifie([5]))

assert verifie([0, 5, 8, 8, 9]) == True
assert verifie([8, 12, 4]) == False
assert verifie([-1, 4]) == True
assert verifie([5]) == True


print()

#Exercice 2
urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if resultat.get(bulletin):
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale

election = depouille(urne)
print("Les élections donne : ", election)
print("Le ou les vainqueur sont : ", vainqueur(election))

assert depouille(urne) == {'A': 3, 'B': 4, 'C': 3}
assert vainqueur(election) == ['B']