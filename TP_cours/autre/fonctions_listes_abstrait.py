def lireElements(lst, position):
    return lst[position]

def insererElement(x,lst,position):
    list2 = []
    for i in range(len(lst)):
        list2.append(lst[i])
    list2[position] = x
    for i in range(position, len(lst)):
        list2.append(lst[i])
    return list2

def supprmerElement(lst, position):
    list2 = []
    for i in range(position):
        list2.append(lst[i])
    for i in range(position+1,len(lst)):
        list2[i-1].append(lst[i])
    return list2

