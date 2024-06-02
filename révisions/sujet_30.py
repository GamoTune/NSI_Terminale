#Exercice 1

def fusion(tab1, tab2):
    n1 = len(tab1)
    n2 = len(tab2)
    i1 = 0
    i2 = 0
    tab = []
    print(tab)
    while i1 < n1 and i2 < n2:
        if tab1[i1] < tab2[i2]:
            tab.append(tab1[i1])
            i1 += 1
        else:
            tab.append(tab2[i2])
            i2 += 1
    while i1 < n1:
        tab.append(tab1[i1])
        i1 += 1
    while i2 < n2:
        tab.append(tab2[i2])
        i2 += 1
    return tab

print(fusion([-2, 4], [-3, 5, 10]))