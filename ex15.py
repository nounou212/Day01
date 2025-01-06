import random

nombre_mystere = random.randint(1, 1000)
tentatives = 10
print(f"J'ai choisi un nombre entre 1 et 1000. Vous avez {tentatives} tentatives pour le deviner.")
while tentatives > 0:
    proposition = int(input("Votre proposition : "))

    if proposition < nombre_mystere:
        print("Trop bas !")
    elif proposition > nombre_mystere:
        print("Trop haut !")
    else:
        print("Bravo, vous avez deviné !")
        break  

    tentatives -= 1  

    if tentatives == 0:
        print(f"Dommage, vous n'avez plus d'essais. Le nombre mystère était {nombre_mystere}.")