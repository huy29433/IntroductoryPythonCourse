import math


def main():
    myList = ["Dusky", "Joe", "Hartington"]
    print("### ELEMENTE IN MODUL MATH:")
    print(dir(math))

    print()

    print("### ELEMENTE IN KLASSE LIST:")
    print(dir(myList))

    print(help(math.factorial))  # Berechnet Fakultät 4! -> 4 * 3 * 2 * 1
    print(help(math.radians))  # Konvertiert Winkel von Grad nach Radians -> deg_Rad = 3.14/180 * deg_Grad
    print(help(myList.index))  # Gibt Index der Liste zurück - Joe -> 1; Hartington -> 2 ...
    print(help(myList.clear))  # Leert Liste

    print()
    print("Umwandlung 180 Grad -> Radians")
    print(math.radians(180))  # Pi
    print()
    print("Index von Joe")
    print(myList.index("Joe"))
    print()
    print("Loeschen Liste")
    print(myList)
    myList.clear()
    print(myList)

    print()
    print("Fakultaet 4")
    print(math.factorial(4))


if __name__ == "__main__":
    main()
