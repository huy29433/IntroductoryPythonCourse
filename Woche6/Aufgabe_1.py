def chainGenerator2(*chainElements, sep = '-'):
    returnString = ""
    for indexOfElement in range(len(chainElements)):
        returnString += str(chainElements[indexOfElement])
        if indexOfElement != len(chainElements) - 1:        # Stoppe bei vorletztem Element
            returnString += sep
    return returnString


def chainGenerator(*chainElements, sep = '-'):
    returnString = ""
    for element in chainElements:
        returnString += str(element)
        returnString += sep
    returnString = returnString[:-len(sep)]
    return returnString


def chainGenerator3(*chainElements, sep = '-'):
    # Setzt voraus, dass mindestens 1 Element vorhanden ist
    returnString = str(chainElements[0])
    for element in chainElements[1:]:
        returnString += sep
        returnString += str(element)
    return returnString


def main():
    print(chainGenerator(1, 2, 3))  # Ausgabe: 1-2-3
    print(chainGenerator(1, 2, 3, 4, sep="~~~"))  # Ausgabe: 1~~~2~~~3~~~4
    print(chainGenerator())

    print(chainGenerator2(1, 2, 3))  # Ausgabe: 1-2-3
    print(chainGenerator2(1, 2, 3, 4, sep="~~~"))  # Ausgabe: 1~~~2~~~3~~~4
    print(chainGenerator2())

    print(chainGenerator3(1, 2, 3))  # Ausgabe: 1-2-3
    print(chainGenerator3(1, 2, 3, 4, sep="~~~"))  # Ausgabe: 1~~~2~~~3~~~4
#    print(chainGenerator3())           # does not work

if __name__ == "__main__":
    main()
