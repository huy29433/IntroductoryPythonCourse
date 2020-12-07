import random


def sort_list_long(unsortedList):
    for i in range(len(unsortedList)):
        minValue = min(unsortedList[i:])
        indexOfMinValue = unsortedList.index(minValue, i)
        unsortedList[i], unsortedList[indexOfMinValue] = unsortedList[indexOfMinValue], unsortedList[i]


def sort_list(unsortedList):
    for i in range(len(unsortedList)):
        indexOfNextMinValue = unsortedList.index(min(unsortedList[i:]), i)
        unsortedList[i], unsortedList[indexOfNextMinValue] = unsortedList[indexOfNextMinValue], unsortedList[i]


def main():
    sampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    randomList = random.sample(sampleList, 10)
    print(randomList)
    sort_list(randomList)
    print(randomList)


if __name__ == "__main__":
    main()
