
entree = input("Nombres séparés par des virgules : ")
liste_str = entree.split(",")
liste_nombres = [float(x.strip()) for x in liste_str]

for i in range(len(liste_nombres)):
    min_index = i
    for j in range(i + 1, len(liste_nombres)):
        if liste_nombres[j] < liste_nombres[min_index]:
            min_index = j
    liste_nombres[i], liste_nombres[min_index] = liste_nombres[min_index], liste_nombres[i]

print("Liste triée :", liste_nombres)