x = float(input("x: "))
op = input("Opération (+ - * /): ")
y = float(input("y: "))

if op == '+': print(x + y)
elif op == '-': print(x - y)
elif op == '*': print(x * y)
elif op == '/':
    print(x / y if y != 0 else "Erreur : division par zéro")
else:
    print("Opération invalide")