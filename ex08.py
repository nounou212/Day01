a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))
c = float(input("Entrez le troisième nombre : "))

plus_grand = a

if b > plus_grand:
    plus_grand = b
if c > plus_grand:
    plus_grand = c

print("Le plus grand nombre est :", plus_grand)