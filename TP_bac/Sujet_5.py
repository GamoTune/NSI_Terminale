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
        if tab[i] == 6: num_of_six += 1
        if num_of_six >= 2: return True
    return False

lancer1 = lancer(5)
print("Le lancer 1 donne : ", lancer1)
print("Y a t'il une paire de 6 : ", paire_6(lancer1))

lancer2 = lancer(5)
print("Le lancer 2 donne : ", lancer2)
print("Y a t'il une paire de 6 : ", paire_6(lancer2))

lancer3 = lancer(3)
print("Le lancer 3 donne : ", lancer3)
print("Y a t'il une paire de 6 : ", paire_6(lancer3))

lancer4 = lancer(0)
print("Le lancer 4 donne : ", lancer4)
print("Y a t'il une paire de 6 : ", paire_6(lancer4))


print()
print("---------------------------------------------")
print()


#Exercice 2

img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]

def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''

    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            L[i][j] = 255-image[i][j]
    return L

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil
       et 1 sinon'''

    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            if image[i][j] < seuil :
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L


img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]
print("L'images est : ", img)
print("Le nombre de ligne dans l'image est : ", nbLig(img))
print("Le nombre de colone dans l'image est : ", nbCol(img))
print("Le negatif de l'image est : ", negatif(img))
print("Le binaire de l'image, avec un seuil a 120 est : ", binaire(img,120))


assert nbLig(img) == 4
assert nbCol(img) == 5
assert negatif(img) == [[235, 221, 1, 110, 249], [232, 131, 18, 30, 186], [58, 81, 48, 230, 168], [0, 255, 231, 58, 66]]
assert binaire(img,120) == [[0, 0, 1, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 0, 0, 1, 1]]