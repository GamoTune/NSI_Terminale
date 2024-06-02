#Exercice 1

def nb_repetitions(elt, tab):
    occu = 0
    for i in tab:
        if elt == i:
            occu += 1
    return occu

print(nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']))


#Exercice 2

def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    bin_a = ''
    while a > 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a

print(binaire(77))