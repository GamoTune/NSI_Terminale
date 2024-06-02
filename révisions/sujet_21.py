def recherche_motif(motif, texte):
    occurances = []
    for i in range(len(texte)):
        if texte[i:i+len(motif)] == motif:
            occurances.append(i)
    return occurances

print(recherche_motif("ab", "abracadabraab"))


#Exercice 2

adj = [[1, 2], [0, 3], [0], [1], [5], [4]]

def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x not in acc:
        acc.append(x)
        for y in adj[x]:
            parcours(adj, y, acc)

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x, acc)
    return acc