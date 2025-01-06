n = int(input("Entrez un nombre entier : "))
factoriel = 1

for i in range(1, n+1):
    factoriel *= i

print("Le factoriel de", n, "est :", factoriel)