import random
import string

longueur = int(input("Longueur du mot de passe (nombre de caractères) ? "))
caracteres = string.ascii_letters + string.digits + string.punctuation
mot_de_passe = "".join(random.choice(caracteres) for _ in range(longueur))
print("Votre mot de passe est :", mot_de_passe)