# Matchmaking
import random
import datetime
# Nicht optimiert, aber funktionsfähig
# Muss Liste zweimal durchgehen


def findMatchesVersion1(listOfSocks):
    matches = []
    for i in range(len(listOfSocks)):
        foundIndex = -1
        for j in range(len(listOfSocks)):
            if i == j:
                continue
            if listOfSocks[i] == listOfSocks[j]:
                foundIndex = j
                break
        matches.append(foundIndex)
    return matches


#Setzt gleich 2 Indizes gleichzeitig, spart sich "doppeltes" Durchlaufen der gleichen Socken


def findMatchesVersion2(listOfSocks):
    matches = [-1 for i in listOfSocks]

    for i in range(len(listOfSocks)):
        if matches[i] != -1:
            continue

        for j in range(len(listOfSocks)):
            if i == j:
                continue
            if listOfSocks[i] == listOfSocks[j]:
                matches[j] = i
                matches[i] = j
                break
    return matches


# Ausnutzen der Implementation von Dicts in Python führt zu sehr guter Beschleunigung


def findMatchesVersion3(listOfSocks):
    matches = [-1 for i in listOfSocks]
    dictOfSocks = dict()

    for i in range(0, len(listOfSocks)):
        if matches[i] != -1:
            continue
        if listOfSocks[i] in dictOfSocks:
            matches[dictOfSocks[listOfSocks[i]]] = i
            matches[i] = dictOfSocks[listOfSocks[i]]
            continue
        else:
            dictOfSocks[listOfSocks[i]] = i

    return matches

def main():
    listOfSocks = []
    counter = -1
    for i in range(10000):
        if i % 2 == 0:
            counter += 1
        listOfSocks.append(counter)
    random.shuffle(listOfSocks)
#    print(listOfSocks)

    start = datetime.datetime.now()         # Etwa 10 Sekunden für 10000 Socken
    matches1 = findMatchesVersion1(listOfSocks)
    print(datetime.datetime.now() - start)
    print(matches1)

    start = datetime.datetime.now()         # Etwa 7 Sekunden für 10000 Socken
    matches2 = findMatchesVersion2(listOfSocks)
    print(datetime.datetime.now() - start)
    print(matches2)

    start = datetime.datetime.now()         # etwa 0,004 Sekunden für 10000 Socken
                                            # Test für 1.000.000 Socken: Unter 1 Sekunde *party*
                                            # Test für 1.000.000.000 Socken: Etwa: -> Abgebrochen, da Erstellen der Socken zu lange dauert
    matches3 = findMatchesVersion3(listOfSocks)
    print(datetime.datetime.now() - start)
    print(matches3)

    if matches1 == matches2 and matches2 == matches3:
        print("Alle Versionen liefern das gleiche Ergebnis")



if __name__ == "__main__":
    main()
