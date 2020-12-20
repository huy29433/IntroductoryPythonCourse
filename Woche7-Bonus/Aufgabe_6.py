# Eingabe: "1, 2, 3, 4, "
# Ausgabe: [1, 2, 3, 4]


def stringToNumber(string):
    try:
        return int(string)
    except ValueError:
        return float(string)

def main():
    inputString = input("Kommagetrennte Zahlen: ")
    inputString.replace(" ", "")
    splittedInputString = inputString.split(",")
    numberList = [stringToNumber(string) for string in splittedInputString]
    print(numberList)


if __name__ == "__main__":
    main()
