#Exercice 1


def correspond(mot, mot_a_trous):
    if len(mot) != len(mot_a_trous):
        return False
    for i in range(len(mot)):
        if mot[i] != mot_a_trous[i] and mot_a_trous[i] != '*':
            return False
    return True

print(correspond('AUTO', '*UT*'))


#Exercice 2

def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à un plan d'envoi de messages (ici entre les personnes A, B, C, D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et False sinon.'''
    expediteur = 'A'
    destinataire = plan['A']
    nb_destinataires = 1
    while destinataire != expediteur: 
        destinataire = plan[destinataire]
        nb_destinataires += 1
    return nb_destinataires == len(plan)


print(est_cyclique({'A':'E','F':'C','C':'D','E':'B','B':'F','D':'A'}))