def main():
    listOfPersons = []
    listOfPersons.append(["Peter", 19, 1.8])
    listOfPersons.append(["Jasmin", 20, 1.63])
    listOfPersons.append(["Alex", 22, 1.93])

    print(listOfPersons)
    listOfPersons.sort()
    print(listOfPersons)

    # Mit bisherigem Wissen -> Reihenfolge der Einträge ändern; [Name, Alter, Höhe] -> Das erste Element wird sortiert
    # Eigentlich -> key - parameter der Liste Sort verwenden

    def getThirdElement(list):
        return list[2]

    listOfPersons.sort(key=getThirdElement)
    print(listOfPersons)


if __name__ == "__main__":
    main()
