import random
#Exercice 1

def lancer(n):
    lst = []
    while n != 0:
        lst.append(random.randint(1,6))
        n -= 1
    return lst

def paire_6(tab):
    num_of_six = 0
    for i in range(len(tab)):
        if tab[i] == 2: num_of_six += 1
        if num_of_six >= 2: return True
    return False

lancer1 = lancer(5)
print(lancer1)
print(paire_6(lancer1))