mot = input("Entrez un mot : ")

if mot == mot[::-1]:
    print("C'est un palindrome.")
else:
    print("Ce n'est pas un palindrome.")