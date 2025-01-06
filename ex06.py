import random

nombre_secret = random.randint(1, 100)

print("J'ai choisi un nombre entre 1 et 100. Devinez lequel !")

while True:
    essai = int(input("Votre proposition : "))
    
    if essai < nombre_secret:
        print("Trop bas !")
    elif essai > nombre_secret:
        print("Trop haut !")
    else:
        print("Bravo, vous avez deviné !")
        break