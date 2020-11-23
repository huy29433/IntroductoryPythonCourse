

def main():
    Nst1 = "(-b+(b**2-4*a*c)**0.5)/(2*a)"
    Nst2 = "(-b-(b**2-4*a*c)**0.5)/(2*a)"

    a = 0
    b = 0
    c = 0
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        x1 = eval(Nst1)
        x2 = eval(Nst2)

        print(f"Nst1: {x1}, Nst2: {x2}")
        # Warum spezielle Version für nicht-reellwertige Ergebnisse?

    except Exception as e:
        print(f"Error in Eingabe\n{e}")


if __name__ == "__main__":
    main()
