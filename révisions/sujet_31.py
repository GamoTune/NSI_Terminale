#Exercice 1

def multiplication(n1, n2):
    r = 0
    if n1 < 0:
        return -multiplication(-n1, n2)
    if n2 < 0:
        return -multiplication(n1, -n2)
    
    for _ in range(n2):
        r += n1
    return r

print()
print(multiplication(-2, 6))
print()