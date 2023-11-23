#Exercise 1

def nb_repetitions(elt, tab):
    nb = 0
    for i in range(len(tab)):
        if tab[i] == elt:
            nb = nb + 1
    return nb

assert nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]) == 3
assert nb_repetitions('A', [ 'B', 'A', 'B', 'A', 'R']) == 2
assert nb_repetitions(12, [1, '! ', 7, 21, 36, 44]) == 0
print("le nombre de répétion de 5 dans [2, 5, 3, 5, 6, 9, 5] est : ", nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]))
print("le nombre de répétion de A dans [ 'B', 'A', 'B', 'A', 'R'] est : ", nb_repetitions('A', [ 'B', 'A', 'B', 'A', 'R']))
print("le nombre de répétion de 12 dans [1, '! ', 7, 21, 36, 44] est : ", nb_repetitions(12, [1, '! ', 7, 21, 36, 44]))



#Exercice 2
def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a != 0 :
        bin_a = str(a%2) + bin_a
        a = a // 2
    return bin_a

assert binaire(0) == '0'
assert binaire(77) == '1001101'
print("la valeur binaire de 0 est : ", binaire(0))
print("la valeur binaire de 77 est : ", binaire(77))