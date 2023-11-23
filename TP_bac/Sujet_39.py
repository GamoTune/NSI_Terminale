#Exercice 1

def fibonacci(n):
    liste=[1,1]
    while len(liste)<n : liste.append(liste[-2]+liste[-1])
    return liste[-1]

print("fibonacci de 45 =",fibonacci(45))

print()


#Exercice 2

def pantheon(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = []

    for i in range(len(notes)) :
        if notes[i] == note_maxi :
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]

    return (note_maxi,meilleurs_eleves)



eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]

print(f"pantheon de {eleves_nsi} avec {notes_nsi} est : ",pantheon(eleves_nsi, notes_nsi))