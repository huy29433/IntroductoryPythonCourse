#       0 | 1  | 2
#       3 | 4  | 5
#       6 | 7  | 8
#       9 | 10 | 11


# Zelle 3 -> 2
# Zelle 6 -> 5
# Zelle 2 -> 1
# Zelle 5 -> 4

b = int(input("Wie breit soll die Tabelle sein?"))
h = int(input("Wie hoch soll die Tabelle sein?"))

id = int(input("Welche Zellenposition soll ausgegeben werden?"))

Zeile = id // b
Spalte = id % b

print(f"Zeile: {Zeile} \t Spalte: {Spalte}")
