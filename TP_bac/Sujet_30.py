#Exercice 1

def moyenne(tab):
    somme = 0
    for i in tab:
        somme = somme + i
    return somme / len(tab)

print("La moyenne de [1.0] est : ", moyenne([1.0]))
print("La moyenne de[1.0, 2.0, 4.0] est : ", moyenne([1.0, 2.0, 4.0]))

assert moyenne([1.0]) == 1.0
assert moyenne([1.0, 2.0, 4.0]) == 7.0 / 3

print()
print("-----------------------------")
print()


#Exercice 2

def binaire(a):
    bin_a = str(a % 2)
    a = a // 2
    while a > 0 :
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a



print("Le binaire de 83 est : ", binaire(83))
print("Le binaire de 127 est : ", binaire(127))
print("Le binaire de 0 est : ", binaire(0))

assert binaire(83) == '1010011'
assert binaire(127) == '1111111'
assert binaire(0) == '0'