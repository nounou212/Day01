notes = [float(x) for x in input("Entrez les notes séparées par des virgules (ex : 12, 15, 10.5) : ").split(",")]
print("Moyenne :", sum(notes) / len(notes))