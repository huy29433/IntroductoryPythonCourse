def isInList(tmp_searchTerm, tmp_list):
    lengthOfList = len(tmp_list)
    if lengthOfList == 1:
        return tmp_searchTerm == tmp_list[0]

    else:
        halfLengthOfList = lengthOfList // 2
        if tmp_searchTerm < tmp_list[halfLengthOfList]:
            newList = tmp_list[:halfLengthOfList]
        else:
            newList = tmp_list[halfLengthOfList:]
        return isInList(tmp_searchTerm, newList)


def main():
    data = [1, 5, 6, 7, 8, 42, 96, 666, 1337, 2112]

    searchTerm = 42

    print(isInList(searchTerm, data))


    # Es müssen durchsucht werden:
    # Im ersten Schritt wird auf die Hälfte der Elemente gekürzt.
    # Im zweiten Schritt ebenso
    # Bei N = 3 : 2, 1                                          3 Vergleiche
    # Bei N = 8 : 4, 2, 1 #                                     4  Vergleiche
    # Bei N = 100: 50, 25, 13, 6, 3, 2, 1 #                     8 Vergleiche
    # Bei N = 1000: 500, 250, 125, 63, 32, 16, 8, 4, 2, 1 #     11 Vergleiche

    # Iterativ: Maximal



if __name__ == "__main__":
    main()
