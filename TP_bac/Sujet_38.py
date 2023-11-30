#Exercice 1

def correspond(mot, mot_a_trous):
    if (len(mot) == len(mot_a_trous)):
        for i in range(len(mot)):
            if mot[i] == mot_a_trous[i] or mot[i] == '*':
                return True
    return False

print("Le mot INFORMATIQUE correspond à INFO*MA*I*UE : ", correspond('INFORMATIQUE', 'INFO*MA*IQUE'))
print("Le mot AUTOMATIQUE correspond à INFO*MA*IQUE : ", correspond('AUTOMATIQUE', 'INFO*MA*IQUE'))
print("Le mot STOP correspond à S* : ", correspond('STOP', 'S*'))
print("Le mot AUTO correspond à *UT* : ", correspond('AUTO', '*UT*'))

assert correspond('INFORMATIQUE', 'INFO*MA*IQUE') == True
assert correspond('AUTOMATIQUE', 'INFO*MA*IQUE') == False
assert correspond('STOP', 'S*') == False
assert correspond('AUTO', '*UT*') == True

print("--------------------------------------------------------------------")

def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant à un plan d'envoi de messages (ici entre les personnes A, B, C, D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et False sinon.
    '''
    expediteur = 'A'
    destinataire = plan[ expediteur ]
    nb_destinaires = 1
    
    while destinataire != expediteur:
        destinataire = plan[ destinataire ]
        nb_destinaires += 1

    return nb_destinaires == len(plan)


print("Le plan d'envoi de messages est cyclique : ", est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F','D':'C'}))
print("Le plan d'envoi de messages est cyclique : ", est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F','D':'A'}))
print("Le plan d'envoi de messages est cyclique : ", est_cyclique({'A':'B', 'F':'C', 'C':'D', 'E':'A', 'B':'F','D':'E'}))
print("Le plan d'envoi de messages est cyclique : ", est_cyclique({'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F','D':'E'}))

assert est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F','D':'C'}) == False
assert est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F','D':'A'}) == True
assert est_cyclique({'A':'B', 'F':'C', 'C':'D', 'E':'A', 'B':'F','D':'E'}) == True
assert est_cyclique({'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F','D':'E'}) == False
