#Exo 1

def multiplication(n1,n2):
    s=0
    if n1==0 or n2==0:
        return 0
    if n1<0:
        return -multiplication(-n1,n2)
    if n2<0:
        return -multiplication(n1,-n2)
    for i in range(n2):
        s = s+n1
    return s

print("La multiplication de 3 avec 5 est : ",multiplication(3, 5))
print("La multiplication de -4 avec -8 est : ",multiplication(-4, -8))
print("La multiplication de -2 avec 6 est : ",multiplication(-2, 6))
print("La multiplication de -2 avec 0 est : ",multiplication(-2, 0))
assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(-2, 0) == 0


#Exo 2

def chercher(tab, n, i, j):
    if i < 0 or j > len(tab):
        return None
    elif i > j:
        return None
    m = (i + j) // 2
    if tab[m] < n:
        return chercher(tab, n, m+1, j)
    elif tab[m] > n:
        return chercher(tab, n, i, m-1)
    else:
        return m
    
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 10))
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 9, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 6, 0, 5))

assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 10) == None
assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 5) == None
assert chercher([1, 5, 6, 6, 9, 12], 9, 0, 5) == 4
assert chercher([1, 5, 6, 6, 9, 12], 6, 0, 5) == 2