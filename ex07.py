phrase = input("Entrez une phrase : ")
voyelles = "aeiouAEIOU"
compteur = 0

for lettre in phrase:
    if lettre in voyelles:
        compteur += 1

print("Le nombre de voyelles dans la phrase est :", compteur)