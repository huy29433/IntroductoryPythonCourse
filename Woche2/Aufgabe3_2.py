def func(x):
    return x ** 2 + 3 * x - 5 == 0


equation = "x^2 + 3*x - 5 = 0"

print(f"Pruefe ob eingegebene Zahl, LSG zu Gleichung {equation} ist")
val_for_x = float(input("Welche Zahl soll geprueft werden?"))

result_string = "Ihre Eingabe ist "
if not func(val_for_x):
    result_string += "k"

result_string += f"eine Loesung zu {equation}"

print(result_string)