equation = "x^2 + 3*x - 5 = 0"

print(f"Pruefe ob eingegebene Zahl, LSG zu Gleichung {equation} ist")
val_for_x = float(input("Welche Zahl soll geprueft werden?"))

if (val_for_x ** 2 + 3 * val_for_x - 5 == 0):
    print(f"Ihre Eingabe ist eine Loesung zu {equation}")
else:
    print(f"Ihre Eingabe ist keine Loesung zu {equation}")