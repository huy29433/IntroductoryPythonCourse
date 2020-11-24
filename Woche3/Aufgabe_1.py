

def main():
    Diskriminante = "b**2-4*a*c"
    Nst1 = "(-b+(Diskriminante)**0.5)/(2*a)"
    Nst2 = "(-b-(Diskriminante)**0.5)/(2*a)"

    a = 0
    b = 0
    c = 0
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))

        Diskriminante = eval(Diskriminante)
        if (Diskriminante < 0):
            print("Ergebnisse nicht nur reellwertig")

        x1 = eval(Nst1)
        x2 = eval(Nst2)

        print(f"Nst1: ({x1}/0)\nNst2: ({x2}/0)")

    except Exception as e:
        print(f"Error in Eingabe\n{e}")


if __name__ == "__main__":
    main()
